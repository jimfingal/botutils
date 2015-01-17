import os

class OAuthTokens(object):

    def __init__(self, app_name):
        self.consumer_key = os.environ.get(app_name + '_CONSUMER_KEY')
        self.consumer_secret = os.environ.get(app_name + '_CONSUMER_SECRET')
        self.access_token = os.environ.get(app_name + '_ACCESS_TOKEN')
        self.access_token_secret = os.environ.get(app_name + '_ACCESS_TOKEN_SECRET')

def check_config(app_name):

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

        raise Exception("Error: Environment variables not set")


def get_redis_url(app_name):
    return os.getenv(app_name + '_REDIS_URL', 'redis://localhost:6379')

def get_mongo_uri(app_name):
    return os.environ.get(app_name + '_MONGO_URI', '')

def get_screen_name(app_name):
    return os.environ.get(app_name + '_SCREEN_NAME')
