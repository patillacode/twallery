# import os
# import sys
import json
import logging

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

import settings

# Variables that contains the user credentials to access Twitter API
from keys import ACCESS_TOKEN
from keys import ACCESS_TOKEN_SECRET
from keys import CONSUMER_KEY
from keys import CONSUMER_SECRET


class Listener(StreamListener):
    """Basic twitter listener: stores/publishes received tweets in redis."""
    def __init__(self, tracker):
        self.tracker = tracker
        # super(Listener, self).__init__(*args, **kwargs)

    def on_data(self, data):
        """
            What to do on the event of receiving data while listening

            Args:
                data: Response form twitter API with the tracked tweet
        """
        # https://dev.twitter.com/overview/api/entities-in-twitter-objects#media
        hashtags = []
        media_url = []
        data = json.loads(data)

        if 'entities' in data and 'hashtags' in data['entities']:
            hashtags = data['entities']['hashtags']
        if 'entities' in data and 'media' in data['entities']:
            for m in data['entities']['media']:
                media_url.append(m['media_url'])

        for h in hashtags:
            if h['text'] in self.tracker.hashtags:
                # create data to be published in channel
                data_to_publish = {}
                data_to_publish.update({'event': 'tweet'})
                data_to_publish.update({'hashtag': h['text']})
                data_to_publish.update(
                    {'text': data['text'].encode('utf-8')})
                user_data = {'id': data['user']['id_str'],
                             'name': data['user']['name'].encode('utf-8'),
                             'screen_name': data['user']['screen_name'],
                             'avatar_url': data['user']['profile_image_url']
                             }
                data_to_publish.update({'user_data': user_data})
                data_to_publish.update({'media_url': media_url})
                # publish data
                self.tracker.publish_data(data_to_publish)

        return True

    def on_error(self, status):
        """
            Log if an error occurs when accessing the API

            Args:
                status (int): HTTP status code
        """
        logging.error("Listener had problems connecting. Status: {0}".format(
            status))


class Tracker():
    """
        Main class that handles most of our app.

        Attributes:
            redis (Redis): redis connection (settings)
            channel (str): channel unique identifier
            hashtags (list): hashtags to keep track of
            known_items (list): all known attributes of the class
            listener (Listener): Twitter StreamListener
            longest (int): length of longest hashtags (for output purposes)
            stream (Stream): Twitter authenticated stream of data
    """

    def __init__(self, hashtags=[]):
        """
            Args:
                hashtags (list, optional): hashtags entered as parameters
        """
        # Set all static attributes
        self.stream = None
        self.listener = None
        self.hashtags = hashtags
        self.redis = settings.REDIS
        self.channel = settings.REDIS_CHANNEL_NAME

    def publish_data(self, data):
        """

            Publish data/event in a channel

            Args:
                data: data to publish in redis
        """
        # logging.debug("publishing to channel {0}".format(self.channel))
        self.redis.publish(self.channel, json.dumps(data))

    def authenticate(self):
        """
            Authenticate against the Twitter API

            Returns:
                Stream: <Twitter authenticated Stream object>
        """

        # Twitter authentication and connection to Twitter Streaming API
        self.listener = Listener(self)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.stream = Stream(auth, self.listener)

        return self.stream
