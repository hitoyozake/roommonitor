# -* encoding: utf-8 *-

import requests
import json
import os
import logging

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

    def get_channel_message(channelId):
        
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
    token = "xoxb-29094********-***************"
    sc = SlackClient(token=token)
    sc.upload2slack("C8J45QS8Y")
