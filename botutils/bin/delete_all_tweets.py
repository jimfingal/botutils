import tweepy
import os
import time
import sys

 
def oauth_login(consumer_key, consumer_secret, access_token, access_token_secret):
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

    if len(sys.argv) == 1:
        print "Usage: python delete_all_tweets.py [APPNAME]"
        sys.exit(0)

    app_name = sys.argv[1]

    consumer_key = os.environ.get(app_name + '_CONSUMER_KEY')
    consumer_secret = os.environ.get(app_name + '_CONSUMER_SECRET')
    access_token = os.environ.get(app_name + '_ACCESS_TOKEN')
    access_token_secret = os.environ.get(app_name + '_ACCESS_TOKEN_SECRET')

    if not consumer_key or \
            not consumer_secret or \
            not access_token or \
            not access_token_secret:

        print "Error: Environment variables not set"
        print "Please re-run with these in your environment:"
        print "   " + app_name + '_CONSUMER_KEY'
        print "   " + app_name + '_CONSUMER_SECRET'
        print "   " + app_name + '_ACCESS_TOKEN'
        print "   " + app_name + '_ACCESS_TOKEN_SECRET'

        sys.exit(0) 

    api =  oauth_login(consumer_key, consumer_secret, access_token, access_token_secret)
    print "Authenticated as: %s" % api.me().screen_name
    
    batch_delete(api)