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

# Setup tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
print("Starting...")
sleep(1)
os.system("cls") if os.name == "nt" else os.system("clear")


# Create a function that favorites latest 10 tweets on your timeline
def fav_timeline():
    # We will use the cursor to iterate through the tweets
    for tweet in tweepy.Cursor(api.home_timeline).items(500):
        # We will only favorite the tweets that have not been favorited yet
        if not tweet.favorited:
            try:
                tweet.favorite()
                print("Liked: ", tweet.text + "\n")
                sleep(randint(4, 15))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

# Create a function that check latest tweets about #cybersecurity, #hacking, #infosec and favorite them if they have more than 100 retweets
def fav_follow():
    # We will use the cursor to iterate through the tweets
    print("Please enter 4 hashtags!")
    ht1 = input("Enter hashtag 1: ")
    ht2 = input("Enter hashtag 2: ")
    ht3 = input("Enter hashtag 3: ")
    ht4 = input("Enter hashtag 4: ")
    hashtags = (ht1 + " OR " + ht2 + " OR " + ht3 + " OR " + ht4)
    for tweet in tweepy.Cursor(api.search, q=hashtags, lang="en", result_type="latest").items(999):
        # We will only favorite the tweets that have not been favorited yet
        if not tweet.favorited:
            try:
                if tweet.favorite_count >= 2 and tweet.retweet_count >= 1:
                    tweet.favorite()
                    print("Liked: ", tweet.text + "\n")
                    sleep(randint(9, 23))
                    if not tweet.user.following and not tweet.user.followers_count >= 50 and not tweet.user.friends_count >= 100:
                        tweet.user.follow()
                        print("Followed: ", tweet.user.screen_name)
                    sleep(randint(3, 13))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break


# Create a function that follow specified user's followers if user has more than 1000 followers and the follower count is more than followings
def follow_em():
    who_to_follow = input("Put the username to follow their followers: ")
    for follower in tweepy.Cursor(api.followers, screen_name=who_to_follow).items():
        if not follower.following:
            try:
                if follower.followers_count >= 500 and follower.followers_count >= follower.friends_count and not follower.friends_count <= 400:
                    follower.follow()
                    print("Followed: ", follower.screen_name)
                    sleep(randint(16, 42))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
# Main Logic


class main:
    def __init__(self):
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Tiwoto v0.1 | Made by UN5T48L3")
        print("")
        print("What do you want to do?")
        print("1. Favorite your timeline")
        print("2. Favorite tweets about #cybersecurity, #hacking, #infosec and follow if the account has more than 50 followers and 100 follows")
        print("3. Follow other's followers")
        print("4. Exit" + "\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            os.system("cls") if os.name == "nt" else os.system("clear")
            fav_timeline()
        elif choice == 2:
            os.system("cls") if os.name == "nt" else os.system("clear")
            fav_follow()
        elif choice == 3:
            os.system("cls") if os.name == "nt" else os.system("clear")
            follow_em()
        elif choice == 4:
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
        exception = input("Do you want to try again? (y/n)" + "\n")
        if exception == "y":
            main()
        else:
            os.system("cls") if os.name == "nt" else os.system("clear")
            print("Exiting...")
            sleep(2)
            os.system("cls") if os.name == "nt" else os.system("clear")
            exit()