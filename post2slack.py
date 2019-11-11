# -* encoding: utf-8 *-

import requests
import json
import os
import logging
import json



class SlackClient:

    token = ""
    url = ""

    def __init__(self, token=""):
        self.token=token
        pass

    """
    """
    def upload2slack(self, channelId):
        abspath=os.path.abspath("./tmpOutput.png")
        file = {"file":open(abspath, "rb")}
        logging.info("file detail: {0}".format(abspath))
        payload = {"token": self.token, "title":"test",\
            "filename":"tmpOutput.png",\
            "initial_comment": "test",\
            "text":"test upload", "channels":channelId }

        # data = request.body params = urlに接続
        try:
            resp = requests.post("https://slack.com/api/files.upload", data=payload, files=file)
        except:
            return False

        return  True


    def generate_payload(self, channelId, type):
        payload = {
            "token" : self.token,
            "channels" : channelId,
        }

        return payload


    def get_channel_message(self, channelId):
        payload = {
            "token" : self.token,
            "channel" : channelId,
            "count" : 100
        }

        resp = requests.get("https://slack.com/api/channels.history", params=payload)

        print(resp.text)

        return True



    def post_message(self, channelId, text, user):
        payload = {
            "token": self.token,
            "channels": channelId,
            "text": text,
            "user": user
        }
        return True






if __name__ == '__main__':

    settings = {}

    with open("settings.json") as f:
        settings = json.load(f)



    token = settings["token"]# "xoxb-29094********-***************"
    # bot access token
    sc = SlackClient(token=token)
    sc.get_channel_message("C8J45QS8Y")
    # sc.upload2slack("C8J45QS8Y")
