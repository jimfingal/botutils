from tweepy import OAuthHandler
from tweepy import API
from config import OAuthTokens

def get_auth(app):
    tokens = OAuthTokens(app)
    auth = OAuthHandler(tokens.consumer_key, tokens.consumer_secret)
    auth.set_access_token(tokens.access_token, tokens.access_token_secret)
    return auth 

def get_api(auth):
    return API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def get_twython(config):
    from twython import Twython

    return Twython(config.consumer_key,
                  config.consumer_secret,
                  config.access_token,
                  config.access_token_secret)
