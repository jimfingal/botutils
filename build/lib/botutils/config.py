import os

class OAuthTokens(object):

    def __init__(self, app_name):
        self.consumer_key = os.environ.get(app_name + '_CONSUMER_KEY')
        self.consumer_secret = os.environ.get(app_name + '_CONSUMER_SECRET')
        self.access_token = os.environ.get(app_name + '_ACCESS_TOKEN')
        self.access_token_secret = os.environ.get(app_name + '_ACCESS_TOKEN_SECRET')

def get_redis_url(app_name):
    return os.getenv(app_name + '_REDIS_URL', 'redis://localhost:6379')

def get_screen_name(app_name):
    return os.environ.get(app_name + '_SCREEN_NAME')
