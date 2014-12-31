import tweepy
import os
import sys


def oauth_login(consumer_key, consumer_secret):
    """Authenticate with twitter using OAuth"""
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    
    verify_code = raw_input("Authenticate at %s and then enter you verification code here > " % auth_url) 
    auth.get_access_token(verify_code)
    
    return auth
 
if __name__ == "__main__":

    if len(sys.argv) == 1:
        print "Usage: python get_access_token.py [APPNAME]"
        sys.exit(0)

    app_name = sys.argv[1]

    consumer_key = os.environ.get(app_name + '_CONSUMER_KEY')
    consumer_secret = os.environ.get(app_name + '_CONSUMER_SECRET')

    if not consumer_key or not consumer_secret:
        print "Error: Environment variables not set"
        print "Please re-run with these in your environment:"
        print "   " + app_name + '_CONSUMER_KEY'
        print "   " + app_name + '_CONSUMER_SECRET'

        sys.exit(0) 


    auth = oauth_login(consumer_key, consumer_secret)
    print "Access Token ::  %s" % auth.access_token
    print "Access Token Secret ::  %s" %  auth.access_token_secret