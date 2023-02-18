import requests
import logging
# Root path for BGG API
root_path = "https://boardgamegeek.com/xmlapi2/"

class User(object):
    """
    Check if user exists on board game geek
    """
    def ___init___(self, username):
        self.username = username


    def CheckIfUserOnBGG(self):
        logging.info(f"Checking for user: {self.username}")
        user_paramater = f"user?{self.username}"
        parameter = root_path + content
        print(parameter)
        r = requests.post(parameter)
        if r.status_code == 200:
            logging.info(f"Response {r}, user exists!")
            return True
        elif r.status_code == 202:
            logging.info(f"Response {r}, server busy... Retrying")
            self.CheckIfUserOnBGG(self.username)
        else:
            logging.info(f"Response {r}, Aborting search")
            return False

    def CheckIfUserExistsLocally(self):
        pass

    def GetBoardGameCollection(self):
        pass


    def GetBoardGameCollection(self):
        pass
