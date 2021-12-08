#! /usr/bin/python

import json
import tweepy
import Genre
import os

def tweet(message):
    """Handles authentication and tweeting."""
    # "Log in"
    auth = tweepy.OAuthHandler(
        os.getenv('API'), 
        os.getenv('API_SECRET')
    )
    auth.set_access_token(
        os.getenv('ACCESS'), 
        os.getenv('ACCESS_SECRET')
    )
    api = tweepy.API(auth)
    # Post message
    api.update_status(message)

def main():
    """Entry point"""
    song = Genre.get_song()
    message = (f'Your Daily Song is: \n{song["title"]} sang by {song["artist"]}')
    #print(message)
    text = tweet(message)
    pass

if __name__ == "__main__":
    main()
