# -* encoding: utf-8 *-

import requests
import json
import os
import logging
import json
import re


class CommandParser:
    def __init__():
        pass


    def validate_command(command, options, args):
        pass

    def parse_options(command, options):
        # お万度ごとに分岐．できればコマンドごとにクラスがあってポリモーフィズムで処理するのが適切
        pass


    def parse_command(self, command):

        if command == "pictpost":
            return (True, "pict", "take a picture and post")

        # parse失敗
        return (False, "", "Can't Parse command")


    def parse_token(self, tokens):
        # command [--option...] [args...]
        itemlist = []

        if len(tokens) < 1:
            return None

        suceeded, command, msg = self.parse_command(tokens[0])

        if succeeded is False:
            return None

        options = []
        args = []

        # 2個目の引数からはoptions or args. optionでなければそれ以降は全部args
        start = 1
        for index, token in enumurate(tokens[start:]):
            if re.search("^--", token):
                options.append(token)
            else:
                args = tokens[start+index:]
                break

        output = {"command": command, "options": options, "args": args}
        logging.info("parse_token result: {0} => {1}".format(tokens, output))

        return output


    def parse_rawstring(self, message):

        tokens = message.split(" ")

        r = self.parse_token(tokens)

        if r is not None:
            command, msg = r[0], r[1]

        logging.info("parse_rawstring command is : {0}".format(command))

        self.parse_token(tokens)




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
