# -* encoding: utf-8 8-

import cv2
import logging
import post2slack as slack
import json


def take_a_picture():
    img = None
    mirror = False
    tmpFilename = "tmpOutput.png"
    try:
        cap = cv2.VideoCapture(1)
        # 一枚だけスクリーンショットを作成する

        ret, frame = cap.read()


        # 鏡像反転
        if mirror is True:
            frame = frame[::, -1]

        if frame is not None:
            logging.info("saved Img")
            cv2.imwrite(tmpFilename, frame)

        img = frame # 最後までうまくいったのでimgにする

    except:
        logging.info("error: exception is raised at get_a_picture")
        print("error")
        return None
    finally:
        if cap is not None:
            cap.release()

    return img

if __name__ == '__main__':

    info = {}

    commandParser = slack.CommandParser()

    with open("channels.json") as f:
        info = json.load(f)

    channelId = info["Workspaces"]["discuss"]["channels"]["general"]["channelId"]
    settings = {}

    with open("settings.json") as f:
        settings = json.load(f)

    token = settings["token"]# "xoxb-29094********-***************"
    client = slack.SlackClient(token)

    response = client.get_channel_message("C8J45QS8Y", False)

    parser = slack.CommandParser()

    for msgs in response["messages"]:
        if msgs["type"] == "message":
            rawstring = msgs["text"]
            r = parser.parse_rawstring(rawstring)
            print("text: {0}, parse result: {1}".format(rawstring, r))

            if r is not None and r["command"] == "pictpost":
                img = take_a_picture()

                if img is not None:
                    param = [int(cv2.IMWRITE_JPEG_QUALITY), 6]
                    result, jpg = cv2.imencode(".jpg", img, param)
                    print(result)
                    print(channelId)
                    r = client.upload2slack(channelId, file=jpg)
                    print(r)


    print("done....")
