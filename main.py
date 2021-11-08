# /usr/bin/env python3

import tweepy
import os
from os.path import join, dirname
from random import randint
from time import sleep
from pathlib import Path
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

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
print("Starting...")
sleep(1)
os.system("cls") if os.name == "nt" else os.system("clear")


def fav_timeline():
    for tweet in tweepy.Cursor(api.home_timeline).items(500):
        if not tweet.favorited:
            try:
                tweet.favorite()
                print("Liked: ", tweet.text + "\n")
                sleep(randint(4, 15))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

def ht_follow():
    print("Please enter 4 hashtags!")
    ht1 = (str(input("Enter hashtag 1: ")))
    ht2 = (str(input("Enter hashtag 2: ")))
    ht3 = (str(input("Enter hashtag 3: ")))
    ht4 = (str(input("Enter hashtag 4: ")))
    for tweet in tweepy.Cursor(api.search, q=ht1 + " OR " + ht2 + " OR " + ht3 + " OR " + ht4, lang="en",  ).items(500):
        if not tweet.favorited and not tweet.retweeted:
            try:
                if tweet.retweet_count >= 9 and not tweet.user.following:
                    tweet.user.follow()
                    print("Followed: ", tweet.user.screen_name + "\n")
                    sleep(randint(1, 5))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

def ht_fav():
    print("Please enter 4 hashtags!")
    ht1 = (str(input("Enter hashtag 1: ")))
    ht2 = (str(input("Enter hashtag 2: ")))
    ht3 = (str(input("Enter hashtag 3: ")))
    ht4 = (str(input("Enter hashtag 4: ")))
    for tweet in tweepy.Cursor(api.search, q=ht1 + " OR " + ht2 + " OR " + ht3 + " OR " + ht4, lang="en" ).items(500):
        if not tweet.favorited:
            try:
                if tweet.retweet_count >= 9:
                    tweet.favorite()
                    print("Liked: ", tweet.text + "\n")
                    sleep(randint(2, 5))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

def save_following():
    os.system("cls") if os.name == "nt" else os.system("clear")
    print("Your username is: ", (api.me().screen_name))
    who_to_follow = input("If you don't specify a username it will save your following list: ")
    if who_to_follow == "":
        who_to_follow = api.me().screen_name
        with open("following.txt", "w") as f:
            for user in tweepy.Cursor(api.friends, screen_name=who_to_follow, count=200).items():
                    f.write(user.screen_name + "\n")


# Main Logic
class main:
    def __init__(self):
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Tiwoto v0.1 | Made by UN5T48L3")
        print("")
        print("What do you want to do?")
        print("1. Favorite whole your timeline (last 500 tweets)")
        print("2. Fav Hashtags")
        print("3. Follow Users About Those Hashtags")
        print("4. Save following list as a file of a user" + "\n")
        print("5. Exit" + "\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            os.system("cls") if os.name == "nt" else os.system("clear")
            fav_timeline()
        elif choice == 2:
            os.system("cls") if os.name == "nt" else os.system("clear")
            ht_fav()
        elif choice == 3:
            os.system("cls") if os.name == "nt" else os.system("clear")
            ht_follow()
        elif choice == 4:
            os.system("cls") if os.name == "nt" else os.system("clear")
            save_following()
        elif choice == 5:
            os.system("cls") if os.name == "nt" else os.system("clear")
            print("Exiting...")
            sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            exit()
        else:
                print("Invalid choice!" + "\n")
                print("Exiting...")
                sleep(1)
                os.system("cls") if os.name == "nt" else os.system("clear")
                exit()

# run the main function
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Exiting...")
        sleep(1)
        os.system("cls") if os.name == "nt" else os.system("clear")
        exit()
    except Exception as e:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print(e)
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Exiting...")
        sleep(2)
        os.system("cls") if os.name == "nt" else os.system("clear")
        exit()