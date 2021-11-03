#! /usr/bin/python

import json
import tweepy

def load_credentials():
    """Load keys file"""
    # Find the test accounts credentials, open them
    file = open("../.secrets/100-keys.json")
    # Parse JSON in file
    credentials = json.load(file)
    # Return credentials
    return credentials

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
    pass

if __name__ == "__main__":
    main()