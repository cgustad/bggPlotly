from bs4 import BeautifulSoup as Soup
import pandas as pd

def parse_games_response(res):
    soup = Soup(res.content)
    games = soup.findAll("item")
    user_data = []
    for game in games:
        id = game.get("objectid")
        user_data.append(id)

    series = pd.Series(user_data)
    return user_data
