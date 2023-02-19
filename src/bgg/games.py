import requests
from bs4 import BeautifulSoup as Soup
root_path = "https://boardgamegeek.com/"

class Game():
    def __init__(self, id):
        self.id = id
        self.data = dict()


def parse_game_page(response):
    soup = Soup(response.text)
    image_path = soup.find("src", class_="rank-number")
    print(image_path)
