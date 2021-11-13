#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
# This file is part of Tiwoto Open Project.                                   #
#                                                                             #
# Tiwoto Open Project is free software: you can redistribute it and/or        #
# modify it under the terms of the GNU General Public License as published by #
# the Free Software Foundation, either version 3 of the License, or (at your  #
# option) any later version.                                                  #
#                                                                             #
# Tiwoto Open Project is distributed in the hope that it will be useful, but  #
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY  #
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for #
# more details.                                                               #
#                                                                             #
# You should have received a copy of the GNU General Public License along     #
# with Tiwoto Open Project. If not, see <http://www.gnu.org/licenses/>.       #
#                                                                             #
###############################################################################
# WARNING:                                                                    #
# If you are not sure about about Twitter API rate limits,                    #
# please do not use this script more than once an hour.                       #
# because if your account reachs Twitter API rate limits too often,           #
# your account might be suspended.                                            #
#                                                                             #
# This program coded by Mehmetcan Yildiz aka UN5T48L3 for fun. ^^             #
###############################################################################


import tweepy
import os
from os.path import join, dirname
from random import randint
from time import sleep
from dotenv import load_dotenv

if 'consumer_key' or "access_token" in os.environ:
    load_dotenv(dotenv_path=join(dirname(__file__), '.env'))
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    consumer_key = os.getenv('consumer_key')
    consumer_secret = os.getenv('consumer_secret')
    access_token = os.getenv('access_token')
    access_token_secret = os.getenv('access_token_secret')
else:
    print("Please set your API keys in the .env file")
    print("Exiting..." + "\n")
    sleep(1)
    os.system("cls") if os.name == "nt" else os.system("clear")
    exit()

print("Starting...")
sleep(1)
os.system("cls") if os.name == "nt" else os.system("clear")

# Tweepy API setup
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def fav_timeline():
    print("Like your timeline: \n")
    i = 0
    value = input("How many tweets you want to like: ")
    while i < int(value):
        for tweet in api.home_timeline():
            try:
                if not tweet.favorited and not i == int(value):
                    tweet.favorite()
                    i += 1
                    print(
                        "🖤 Liked => [https://twitter.com/" + tweet.user.screen_name + "/status/" + tweet.id_str + "]")
                    sleep(randint(2, 11))
            except tweepy.TweepyException as err1:
                print(err1)
                i -= 1
            except StopIteration:
                break
    else:
        print("\n", "Done ✔️", "\n")
        print("🖤 Liked Total Tweets => ", i)
        sleep(2)
        input("Press enter to return main menu")
        MainStuff()


def ht_fav():
    print("Like hashtags: \n")
    ht1 = input(str("Enter a hashtag: "))
    ht2 = input(str("Enter another hashtag: "))
    print("\n")
    i = 0
    value = input("How many tweets you want to like: ")
    while i < int(value):
        for tweet in api.search_tweets(q=ht1 + " OR " + ht2 + " -exclude:retweet", result_type="recent", lang="en"):
            try:
                if not tweet.favorited and not i == int(value) and not tweet.favorite_count >= 10:
                    tweet.favorite()
                    i += 1
                    print(
                        "🖤 Liked => [https://twitter.com/" + tweet.user.screen_name + "/status/" + tweet.id_str + "]")
                    sleep(randint(1, 14))
            except tweepy.TweepyException as err1:
                i -= 1
                print(err1)
            except StopIteration:
                break
    else:
        print("\n", "Done ✔️", "\n")
        print("🖤 Liked Total Tweets => ", i)
        sleep(2)
        input("Press enter to return main menu")
        MainStuff()


def ht_follow():
    print("Follow and like: \n")
    ht1 = input(str("Enter a word or hashtag: "))
    ht2 = input(str("Enter another word or hashtag: "))
    print("\n")
    i = 0
    value = input("How many users you want to follow: ")
    while i < int(value):
        for tweet in api.search_tweets(q=ht1 + " OR " + ht2 + " -exclude:retweet", result_type="recent", lang="en"):
            try:
                if not tweet.user.following and not i == int(value) and not tweet.favorite_count >= 12:
                    tweet.user.follow()
                    i += 1
                    print("➕ Followed => [https://twitter.com/" + tweet.user.screen_name + "]")
                    sleep(randint(2, 39))
            except tweepy.TweepyException as err1:
                i -= 1
                print(err1)
            except StopIteration:
                break
    else:
        print("\n", "Done ✔️", "\n")
        print("👤 Followed Total Users => ", i)
        sleep(2)
        input("Press enter to return main menu")
        MainStuff()


# Check my friends and save to file line by line
def save_following():
    os.system("cls") if os.name == "nt" else os.system("clear")
    # ask if you want to save to file
    print("Do you want to save your following to a file? (y/n)")
    save_friend = input()
    if save_friend == "y":
        # ask for file name
        print("Please enter the file name: ")
        filename = input()
        # save to file
        with open(filename, 'w') as f:
            for friend in tweepy.Cursor(api.get_friends).items():
                f.write(friend.screen_name + "\n")
        print("Saved to " + filename + "!")
        sleep(2)
        MainStuff()
    elif save_friend == "n":
        MainStuff()
    else:
        print("Invalid input")
        sleep(2)
    return


# Unfollow users who don't follow back
def detect_unfollow():
    print("This function is under development")
    sleep(2)
    MainStuff()


# Main Logic
class MainStuff:
    def __init__(self):
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Tiwoto v0.1 | Made by UN5T48L3")
        print("")
        print("What do you want to do?")
        print("1. Timeline likes")
        print("2. Like tweets.")
        print("3. Search and follow users.")
        print("4. Save friends as a list.")
        print("5. Exit" + "\n")
        choice = input("Enter your choice: ")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            print("Invalid input")
            sleep(2)
            MainStuff()
        while choice.isdigit():
            if choice == "1":
                fav_timeline()
            elif choice == "2":
                ht_fav()
            elif choice == "3":
                ht_follow()
            elif choice == "4":
                save_following()
            elif choice == "5":
                exit()
            else:
                print("Invalid input")
                sleep(2)
                MainStuff()


# run the main function
if __name__ == "__main__":
    try:
        MainStuff()
    except KeyboardInterrupt:
        print("Exiting...")
        sleep(0.5)
        exit()
    except Exception as e:
        print("This is the error:", e)
        sleep(0.1)
        exit()
