import cv2

import settings


class Camera(object):
    def __init__(self):
        self._source = cv2.VideoCapture(settings.SOURCE)

    def __del__(self):
        self._source.release()

    def get(self):
        success, image = self._source.read()

        if success:
            success, jpeg = cv2.imencode('.jpg', image)

            if success:
                return jpeg.tobytes()
