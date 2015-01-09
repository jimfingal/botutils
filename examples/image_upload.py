from twython import Twython
import tweepy
import config
import image_processor


class MockStatus(object):

    def __init__(self):

        self.media = "https://pbs.twimg.com/media/B5HG0gWIgAAcyn2.png"
        self.hashtags = set(["tiny"])
        self.sender_screen_name = 'jimfingal'

if __name__ == "__main__":


    mock_status = MockStatus()

    img_out = image_processor.process_image(mock_status)
    message = image_processor.get_message(mock_status)

    print message

    twython = Twython(config.consumer_key,
                config.consumer_secret,
                config.access_token,
                config.access_token_secret)

    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    
    tweetter = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    with open(img_out, 'r') as image_file:
        upload_response = twython.upload_media(media=image_file)
        print upload_response
        media_id = upload_response['media_id']
        twython.update_status(status=message, media_ids=[media_id])
