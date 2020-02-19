"""
--------------------------------------------------------------------------------------------
Program: Launch Alpha
Programmer: Mr. Juniper
GitLab:juniper409
Contact: mrjuniper409@gmail.com
--------------------------------------------------------------------------------------------
"""
from tweet_catcher import tweet
import time
import os

while True:

    provider = (input('What is the launch provider? '))
    seconds = int(input('Seconds between refreshes: '))
    lp_input = provider.lower()

    while True:
        if lp_input == 'spacex':
            tweet('34743251', 'SPACEX OFFICIAL')
            tweet('44196397', 'ELON MUSK')
            tweet('1011352897144180737', 'SPACEX FLEET')
            tweet('17217640', 'SPACEFLIGHT NOW')
            time.sleep(seconds)
            os.system('clear')

        elif lp_input == 'ula' or lp_input == 'united launch alliance':
            tweet('22845770', 'UNITED LAUNCH ALLIANCE OFFICIAL')
            tweet('2882413844', 'TORY BRUNO')
            tweet('17217640', 'SPACEFLIGHT NOW')
            time.sleep(seconds)
            os.system('clear')

        elif lp_input == 'rocket lab' or lp_input == 'rocketlab':
            tweet('91145174', 'ROCKET LAB OFFICIAL')
            tweet('976574172468936704', 'PETER BECK')
            tweet('17217640', 'SPACEFLIGHT NOW')
            time.sleep(seconds)
            os.system('clear')

        elif lp_input == 'help' or lp_input == '?':
            print('The followng providers are accepted:', '\n', '-SpaceX', '\n', '-United launch Alliance -or- ULA', '\n', '-Rocketlab')


        else:
            print('Launch provider not found. Please try again.')
            break