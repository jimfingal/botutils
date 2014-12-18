import tweepy
import os
import time

app_name = ""

consumer_key = os.environ.get(app_name + '_CONSUMER_KEY')
consumer_secret = os.environ.get(app_name + '_CONSUMER_SECRET')
access_token = os.environ.get(app_name + '_ACCESS_TOKEN')
access_token_secret = os.environ.get(app_name + '_ACCESS_TOKEN_SECRET')

 
def oauth_login(consumer_key, consumer_secret):
    """Authenticate with twitter using OAuth"""
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
 
def batch_delete(api):
    print "You are about to Delete all tweets from the account @%s." % api.verify_credentials().screen_name
    print "Does this sound ok? There is no undo! Type yes to carry out this action."
    do_delete = raw_input("> ")
    if do_delete.lower() == 'yes':
        count = 0
        for status in tweepy.Cursor(api.user_timeline).items():
            count += 1
            api.destroy_status(status.id)
            print "%s Deleted: %s" % (count, status.id)
            time.sleep(1)
 
if __name__ == "__main__":
    api = oauth_login(CONSUMER_KEY, CONSUMER_SECRET)
    print "Authenticated as: %s" % api.me().screen_name
    
    batch_delete(api)