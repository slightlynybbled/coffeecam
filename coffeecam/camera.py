import time
import os
import logging

from coffeecam.base_camera import BaseCamera

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    # img_path = str(os.path.realpath(__file__)) + '/static/img/'
    img_path = os.path.dirname(__file__) + '/static/img/'
    paths = []

    for i in range(10):
        paths.append(img_path + str(i) + '.jpg')

    images = [open(path, 'rb').read() for path in paths]

    @staticmethod
    def frames():
        while True:
            time.sleep(0.5)
            yield Camera.images[int(time.time()) % 10]
