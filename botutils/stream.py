import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import logging
import time

class RawListener(StreamListener):
    ''' Overrides on_data to pass raw json instead of parsing status objects '''

    def on_data(self, raw_data):
        """Called when raw data is received from connection.

        Override this method if you wish to manually handle
        the stream data. Return False to stop stream and close connection.
        """
        data = json.loads(raw_data)
        logging.debug(data)

        if 'in_reply_to_status_id' in data:
            if self.on_status(data) is False:
                return False
        elif 'delete' in data:
            delete = data['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'event' in data:
            if self.on_event(data) is False:
                return False
        elif 'direct_message' in data:
            if self.on_direct_message(data['direct_message']) is False:
                return False
        elif 'friends' in data:
            if self.on_friends(data['friends']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(data['limit']['track']) is False:
                return False
        elif 'disconnect' in data:
            if self.on_disconnect(data['disconnect']) is False:
                return False
        elif 'warning' in data:
            if self.on_warning(data['warning']) is False:
                return False
        else:
            logging.error("Unknown message type: " + str(raw_data))

    def on_error(self, status_code):
        logging.error('Received error with status code: %s' % status_code)
        return False

    def on_limit(self):
        logging.error('Limit reached')
        return False

    def on_timeout(self):
        logging.error('Stream Timed out')
        return False

    def on_disconnect(self, notice):
        logging.error('Stream Disconnected: %s' % notice)
        return False

    def on_warning(self, notice):
        """Called when a disconnection warning message arrives"""
        logging.warning('Warning received: %s' % notice)
        return

class RedisPublishListener(RawListener):

    def __init__(self, redis, status_channel, *args, **kwargs):
        self.redis = redis
        self.status_channel = status_channel
        logging.info("Publishing to channel: %s" % self.status_channel)
        super(RedisPublishListener, self).__init__(*args, **kwargs)

    def on_status(self, data):
        """Called when a new status arrives"""
        logging.info("Received tweet: %s" % data['text'])
        tweet = json.dumps(data)
        self.redis.publish(self.status_channel, tweet)
        return True


def run_forever_with_backoff(func, base_backoff=60, backoff_multiplier=2, reset_time=3600):
    last_attempt = time.time()
    current_backoff = base_backoff

    while True:

        last_attempt = time.time()

        try:
            func()
        except Exception as e:
            logging.exception(e)


        now = time.time()

        diff = now - last_attempt

        print "It's been %s since last run" % diff
        # If we recently crashed, back off exponentially, else reset
        if diff < reset_time:
            current_backoff = current_backoff * backoff_multiplier
        else:
            logging.info("It's been more than %s seconds, resetting backoff to %s" % (reset_time, base_backoff))
            current_backoff = base_backoff

        logging.error("Something went wrong, backing off for %s seconds before connecting." % current_backoff)
        time.sleep(current_backoff)


def run_user_stream(consumer_key, consumer_secret, access_token, access_token_secret, listener):

    def enclosed_func():
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener)
        logging.info("Attempting to connect the stream.")
        stream.userstream(_with='user')

    run_forever_with_backoff(enclosed_func)