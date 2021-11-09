# /usr/bin/env python3

import tweepy
import os
from os.path import join, dirname
from random import randint
from time import sleep
from dotenv import load_dotenv
from tweepy.models import Friendship


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
    for tweets in api.home_timeline(exclude_replies=True, include_rts=False, count=500):
        if not tweets.favorited:
            try:
                tweets.favorite()
                print("Liked: ", tweets.text)
                print("By: " + tweets.user.screen_name + "\n")
                sleep(randint(1, 3))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

def ht_follow():
    print("Follow people tweeting about;")
    ht1 = (str(input("Enter hashtag 1: ")))
    ht2 = (str(input("Enter hashtag 2: ")))
    ht3 = (str(input("Enter hashtag 3: ")))
    ht4 = (str(input("Enter hashtag 4: ")))
    for tweet in tweepy.Cursor(api.search, q=ht1 + " OR " + ht2 + " OR " + ht3 + " OR " + ht4 + " -exclude:retweet", result_type="recent", lang="en").items(500):
        try:
            if not tweet.user.following and not tweet.user.friends_count <= 300 and not tweet.user.followers_count <= 999:
                api.create_friendship(tweet.user.id)
                print("Followed ====> [" + tweet.user.screen_name + "] and liked their this tweet:")
                sleep(randint(1, 5))
                tweet.favorite()
                print("https://twitter.com/" + tweet.user.screen_name + "/status/" + tweet.id_str + "\n")
                sleep(randint(2, 12))
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def ht_fav():
    print("Favorite hashtags;")
    ht1 = (str(input("Enter hashtag 1: ")))
    ht2 = (str(input("Enter hashtag 2: ")))
    ht3 = (str(input("Enter hashtag 3: ")))
    ht4 = (str(input("Enter hashtag 4: ")))
    for tweet in tweepy.Cursor(api.search, q=ht1 + " OR " + ht2 + " OR " + ht3 + " OR " + ht4 + " -exclude:retweet", result_type="recent", lang="en").items(500):
        try:
            if not tweet.favorited and not tweet.user.following and not tweet.favorite_count <= 100:
                tweet.favorite()
                print("Favorited ===> [" + tweet.user.screen_name + "]""")
                sleep(randint(1, 2))
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def save_following():
    os.system("cls") if os.name == "nt" else os.system("clear")
    print("Your username is: ", (api.me().screen_name))
    who_to_follow = ""
    if who_to_follow == "":
        who_to_follow = api.me().screen_name
        with open("following.txt", "w") as f:
            for user in tweepy.Cursor(api.friends, screen_name=who_to_follow, count=200).items():
                    f.write(user.screen_name + "\n")

# Unfollow users who don't follow back
def detect_unfollow():
    print("TODO")

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
        print("4. Save following list as a file of a user")
        print("5. Unfollow recently followed. " + "\n")
        print("6. Exit" + "\n")
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
            detect_unfollow()
        elif choice == 6:
            os.system("cls") if os.name == "nt" else os.system("clear")
            print("Exiting...")
            sleep(1)
            os.system("cls") if os.name == "nt" else os.system("clear")
            exit()
        else:
                os.system("cls") if os.name == "nt" else os.system("clear")
                print("Invalid choice!" + "\n")
                print("Exiting...")
                sleep(2)
                os.system("cls") if os.name == "nt" else os.system("clear")
                exit()

# run the main function
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        sleep(0.5)
        exit()
    except Exception as e:
        print(e, "<==== This is the error! Fix it.")
        sleep(0.1)
        exit()