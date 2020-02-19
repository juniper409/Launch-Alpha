import access
import os
import sys
import time
import tweepy

auth = tweepy.OAuthHandler(access.consumer_key, access.consumer_secret)
auth.set_access_token(access.access_token, access.access_token_secret)
api = tweepy.API(auth)
user = api.get_user


#Dividing line variables.

div = '*' * 50
div_title = '*' * 10
sep = '\n'

#tweet structure

def tweet(userID, title):
    print(div + '\n' + title + '\n' + div)
    post = api.get_user(userID)
    print(post.status.text)




#Twitter user - assign variable with needed data.



