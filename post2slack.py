# -* encoding: utf-8 *-

import requests
import json
import os
import logging
import json
import re
import io


class CommandParser:
    def __init__(self):
        pass


    def validate_command(command, options, args):
        pass

    def parse_options(command, options):
        # お万度ごとに分岐．できればコマンドごとにクラスがあってポリモーフィズムで処理するのが適切
        pass


    def parse_command(self, command):

        if command == "pictpost":
            return (True, "pictpost", "take a picture and post")

        # parse失敗
        return (False, "", "Can't Parse command")


    def execute_command(self, command, args, options):



        return True


    def parse_token(self, tokens):
        # command [--option...] [args...]
        itemlist = []

        if len(tokens) < 1:
            return None

        succeeded, command, msg = self.parse_command(tokens[0])

        if succeeded is False:
            return None

        options = []
        args = []

        # 2個目の引数からはoptions or args. optionでなければそれ以降は全部args
        start = 1
        for index, token in enumerate(tokens[start:]):
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


        return self.parse_token(tokens)




class SlackClient:

    token = ""
    url = ""
    workspaces = {}

    def __init__(self, token=""):
        self.token=token

        with open("channels.json") as f:
            self.workspaces = json.load(f)

    """
    """
    def upload2slack(self, channelId, file):
        # abspath=os.path.abspath("./tmpOutput.png")
        # file = {"file":open(abspath, "rb")}
        # logging.info("file detail: {0}".format(abspath))

        filebin = io.BytesIO(file)
        payload = {"token": self.token, "title":"test",\
            "filename":"tmpOutput.png",\
            "initial_comment": "test",\
            "text":"test upload", "channels":channelId }


        # file = {"file":}

        file = {"file": filebin}


        # data = request.body params = urlに接続
        # try:
        resp = requests.post("https://slack.com/api/files.upload", data=payload, files=file)
        # except:
        #     return False

        return  True


    def generate_payload(self, channelId, type):
        payload = {
            "token" : self.token,
            "channels" : channelId,
        }

        return payload


    """
        channel_id_を返す workspace, channel-nameが必要
    """
    def get_channel_id_by_name(self, workspace, name):
        for ws, v in self.workspaces["Workspaces"].items():
            if workspace == ws:
                if name in v["channels"]:
                    return v["channels"][name]["channelId"]

        return None


    def get_channel_message(self, channelId, onlyDiff=True):
        payload = {
            "token" : self.token,
            "channel" : channelId,
            "count" : 100
        }

        resp = requests.get("https://slack.com/api/channels.history", params=payload)
        tj = None
        lastTimeStamp = 0.0



        tmpjson = self.workspaces
        tj = tmpjson
        if "lastTimeStamp" in tmpjson["Workspaces"]["discuss"]["channels"]["general"]:
            lastTimeStamp = float(tmpjson["Workspaces"]["discuss"]["channels"]["general"]["lastTimeStamp"])


        messages = []
        respjson = resp.json()
        print(lastTimeStamp)
        if "messages" in respjson:
            for i in respjson["messages"]:
                if lastTimeStamp < float(i["ts"]) or onlyDiff is False:
                   messages.append(i)


        respjson["messages"] = messages

        if len(messages) > 0:
            lastTimeStamp = messages[0]["ts"]

            with open("channels.json", "w") as f:
                if tj is not None:
                    tmpjson = tj
                    self.workspaces = tj
                    tmpjson["Workspaces"]["discuss"]["channels"]["general"]["lastTimeStamp"] = lastTimeStamp
                    json.dump(tmpjson, f, ensure_ascii=False, indent=2, sort_keys=True, separators=(',', ': '))

        return respjson



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
    rsp = sc.get_channel_message("C8J45QS8Y", False)

    parser = CommandParser()

    for msgs in rsp["messages"]:
        if msgs["type"] == "message":
            rawstring = msgs["text"]
            r = parser.parse_rawstring(rawstring)
            print("text: {0}, parse result: {1}".format(rawstring, r))

    # sc.upload2slack("C8J45QS8Y")
