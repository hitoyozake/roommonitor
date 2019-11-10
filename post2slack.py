# -* encoding: utf-8 *-

import requests
import json
import os
to = ""
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
        print(abspath)
        payload = {"token": self.token, "title":"test",\
            "filename":"tmpOutput.png",\
            "initial_comment": "test",\
            "text":"test upload", "channels":channelId }

        resp = requests.post("https://slack.com/api/files.upload", data=payload, files=file)

        print(resp)

        return  True


if __name__ == '__main__':
    token = "xoxb-29094********-***************"
    sc = SlackClient(token=token)
    sc.upload2slack("C8J45QS8Y")
