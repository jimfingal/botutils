
import tweepy
import os

app_name = "TINY"

consumer_key = os.environ.get(app_name + '_CONSUMER_KEY')
consumer_secret = os.environ.get(app_name + '_CONSUMER_SECRET')

def oauth_login(consumer_key, consumer_secret):
    """Authenticate with twitter using OAuth"""
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()
    
    verify_code = raw_input("Authenticate at %s and then enter you verification code here > " % auth_url) 
    auth.get_access_token(verify_code)
    
    return auth
 
if __name__ == "__main__":
    auth = oauth_login(consumer_key, consumer_secret)
    print "Access Token ::  %s" % auth.access_token
    print "Access Token Secret ::  %s" %  auth.access_token_secret