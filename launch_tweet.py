"""
--------------------------------------------------------------------------------------------
Program: Launch Alpha
Programmer: Mr. Juniper
GitLab:juniper409
Contact: mrjuniper409@gmail.com
--------------------------------------------------------------------------------------------
"""
import access
import os
import sys
import time
import tweepy



line = '-'*10

auth = tweepy.OAuthHandler(access.consumer_key, access.consumer_secret)
auth.set_access_token(access.access_token, access.access_token_secret)
api = tweepy.API(auth)
user = api.get_user


while True:


    #SpaceX
    def spacex_tweet():
        spacex = api.get_user('34743251', number_of_tweets = 2)
        print(line + ' SPACEX ' + str(spacex.status.created_at) + line)
        print(spacex.status.text + '\n')
    #Spaceflight Now
    def sfn_tweet():
        sfn = api.get_user('17217640', number_of_tweets = 2)
        print(line + ' SPACEFLIGHT NOW ' + line)
        print(sfn.status.text + '\n')

    #SpaceX Fleet
    def fleet_tweet():
        fleet = api.get_user('1011352897144180737', number_of_tweets = 2)
        print(line + ' SPACEX FLEET ' + str(fleet.status.created_at) + line)
        print(fleet.status.text + '\n')

    def elon_tweet():
        elon = api.get_user('44196397', number_of_tweets = 2)
        print(line + ' ELON MUSK ' + str(elon.status.created_at) + line)
        print(elon.status.text + '\n')

    def countdown():
        while t:
            mins, sec = divmod(t, 60)
            timer = '{:00}:{:120}'.format(mins, sec)
            print(timer, end='\r')
            time.sleep(120)
        print('Refreshing...')

    spacex_tweet()
    sfn_tweet()
    fleet_tweet()
    elon_tweet()
    #time.sleep(300)

#Countdown to refresh
    def countdown(t):
        while t > 0:
            sys.stdout.write('\rNext Refresh : {}s'.format(t))
            t -= 1
            sys.stdout.flush()
            time.sleep(1)

    countdown(300)


    os.system('clear' if os.name == 'nt' else 'clear')
else:
    print('Something went wrong')
