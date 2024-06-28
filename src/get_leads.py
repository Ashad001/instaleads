import os
import json
from creds import USERNAME, PASSWORD
from instagrapi import Client
from instagrapi.exceptions import ClientLoginRequired, ClientConnectionError
from instagrapi.types import UserShort
from src.utils import convert_to_serializable

class GetLeads:
    def __init__(self):
        os.makedirs("logs", exist_ok=True)
        for dir in ["followers", "following"]:
            os.makedirs(f"logs/{dir}", exist_ok=True)
        self.login()
        
    def login(self):
        try:
            self.api = Client()
            self.api.login(username=USERNAME, password=PASSWORD)
        except ClientLoginRequired as e:
            assert "Username or password is incorrect. Please try again..."
        except ClientConnectionError as e:
            assert "Connection error. Please check your internet connection..."
        except Exception as e:  
            assert f"An error occurred: {e}"
            
    def get_user_id(self, username):
        user_id = self.api.user_id_from_username(username)
        return user_id
        
    def get_followers(self, username, save_to_logs=False):
        user_id = self.get_user_id(username)
        followers_json = self.api.user_followers(user_id=user_id)
        followers = []
        for follower in followers_json.values():
            followers.append({"username": follower.username, "full_name": follower.full_name})
        if save_to_logs:
            with open(f"logs/followers/{username}.csv", "w", encoding="utf-8") as f:
                f.write("username,full_name,is_private\n")
                for follower in followers:
                    f.write(f"{follower['username']},{follower['full_name']}\n")

        return followers
        
    def get_following(self, username, save_to_logs=False):
        user_id = self.get_user_id(username)
        following_json = self.api.user_following(user_id=user_id)
        following = []
        for follow in following_json.values():
            following.append({"username": follow.username, "full_name": follow.full_name})
        if save_to_logs:
            with open(f"logs/following/{username}.csv", "w", encoding="utf-8") as f:
                f.write("username,full_name,is_private\n")
                for follow in following:
                    f.write(f"{follow['username']},{follow['full_name']}\n")
        return following
        

if __name__ == "__main__":
    get_leads = GetLeads()
    followers = get_leads.get_followers("ezsnippet")
    following = get_leads.get_following("ezsnippet")
    print(f"Followers: {followers}")
    print(f"Following: {following}")