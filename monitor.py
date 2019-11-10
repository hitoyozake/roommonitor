# -* encoding: utf-8 8-

import cv2
import logging


def get_a_picture():
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
    get_a_picture()