import requests
import os
import logging
from pathlib import Path
from bs4 import BeautifulSoup as Soup
import pandas as pd
import glob

# Root path for BGG API
root_path = "https://boardgamegeek.com/xmlapi2/"

class User():
    def __init__(self, username):
        self.username = username
        self.response = None

    def SaveUserCollection(self):
        """
        Retrive list of games for spescified user and write series to file
        """
        print(f"Getting collection for: {self.username}")
        # API query for owned games
        collection_parameter = f"collection?username={self.username}&own=[1]"
        parameter = root_path + collection_parameter
        # Response from BGG API
        self.response = requests.post(parameter)
        if self.response.status_code == 200:
            # Normal response
            print(f"Response {self.response}")
            # Write file to csv
            games = parse_games_response(self.response)
            print(f"Found {len(games)} games, saved list locally")
            path_to_file = f"dat/users/{self.username}.csv"
            games.to_csv(path_to_file)
        elif self.response.status_code == 202:
            logging.warning(f"Response {self.response}, server busy... Retrying")
            self.SaveUserCollection()
        else:
            print(f"Response {res}, Aborting search")
            return False




def parse_games_response(res):
    soup = Soup(res.content)
    games = soup.findAll("item")
    user_data = []
    for game in games:
        id = game.get("objectid")
        user_data.append(id)
    series = pd.Series(user_data)
    return series
