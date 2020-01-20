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
#Ask how many seconds for refresh.
    try:
        refresh = int(input("How many seconds between refresh?: "))
        break
    except:
        print("Please enter a number")



while True:

#-----------------MISC-----------------
#Spaceflight Now
    def sfn_tweet():
        sfn = api.get_user('17217640', number_of_tweets = 2)
        print(line + ' SPACEFLIGHT NOW ' + line)
        print(sfn.status.text + '\n')

#-----------------SPACEX-----------------
    #SpaceX
    def spacex_tweet():
        spacex = api.get_user('34743251', number_of_tweets = 2)
        print(line + ' SPACEX OFFICIAL ' + line)
        print(spacex.status.text + '\n')

    #SpaceX Fleet
    def fleet_tweet():
        fleet = api.get_user('1011352897144180737', number_of_tweets = 2)
        print(line + ' SPACEX FLEET ' + line)
        print(fleet.status.text + '\n')

    #Elon Musk (Founder/CEO, SpaceX)
    def elon_tweet():
        elon = api.get_user('44196397', number_of_tweets = 2)
        print(line + ' ELON MUSK ' + line)
        print(elon.status.text + '\n')


#-----------------UNITED LAUNCH ALLIANCE-----------------
    #United Launch Alliance
    def ula_tweet():
        ula = api.get_user('22845770')
        print(line + 'UNITED LAUNCH ALLIANCE OFFICIAL' + LINE)
        print(ula.status.text + '\n')


    #Tory Bruno (CEO, ULA)
    def bruno_tweet():
        bruno = api.get_user('2882413844')
        print(line + 'ROCKETLAB OFFICIAL' + LINE)
        print(bruno.status.text + '\n')

#-----------------Rocket Lab-----------------
    #Rocket Lab
    def rocketlab_tweet():
        rocketlab = api.get_user('91145174')
        print(line + 'ROCKETLAB' + LINE)
        print(rocketlab.status.text + '\n')

    #Peter Beck (Founder/CEO, Rocketlab)
    def peterbeck_tweet():
        peterbeck = api.get_user('976574172468936704')
        print(line + 'ROCKETLAB' + LINE)
        print(peterbeck.status.text + '\n')
    

    spacex_tweet()
    sfn_tweet()
    fleet_tweet()
    elon_tweet()

#Countdown to refresh
    def countdown(t):
        while t > 0:
            sys.stdout.write('\rNext Refresh : {}s'.format(t))
            t -= 1
            sys.stdout.flush()
            time.sleep(1)

    countdown(int(refresh))


    os.system('clear' if os.name == 'nt' else 'clear')
else:
    print('Something went wrong')
