class SimpleTweet(object):

    def __init__(self, json):

        self._raw = json

        self.tweet_id = json.get('id')
        self.sender_id = json['user'].get('id')
        self.sender_screen_name = json['user'].get('screen_name')
        self.text = json.get('text')
        self.in_reply_to_status_id_str = json.get('in_reply_to_status_id_str')

        self._user_mentions_raw = json['entities'].get('user_mentions')
        self._hashtags_raw = json['entities'].get('hashtags')
        self._media_raw = json['entities'].get('media')

        self.media = None
        self.hashtags = set()
        self.user_mentions = set()

        if self._user_mentions_raw:
            self.user_mentions.update([d['screen_name'] for d in self._user_mentions_raw])

        if self._hashtags_raw:
            self.hashtags.update([h['text'] for h in self._hashtags_raw])
 
        if self._media_raw:
            self.media = self._media_raw[0]['media_url_https']

    def __str__(self):
        return str(vars(self))