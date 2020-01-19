"""
--------------------------------------------------------------------------------------------
Program: Launch Alpha
Programmer: Mr. Juniper
GitLab:juniper409
Contact: mrjuniper409@gmail.com
--------------------------------------------------------------------------------------------
"""

import tweepy
import access
 
auth = tweepy.OAuthHandler(access.consumer_key, access.consumer_secret)
auth.set_access_token(access.access_token, access.access_token_secret)
api = tweepy.API(auth)
user = api.get_user

class SimpleListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
    
    def on_error(self, status_code):
        if status_code == 420:
            return False
        else:
            return True


tweepy_listener = SimpleListener()
tweepy_stream = tweepy.Stream(auth = api.auth, listener=tweepy_listener)
tweepy_stream.filter(track=['spacex'])