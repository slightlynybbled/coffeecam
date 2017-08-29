import time
import os
import logging

from coffeecam.base_camera import BaseCamera

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files"""

    img_path = os.path.dirname(__file__) + '/static/img/'
    paths = []

    for i in range(10):
        paths.append(img_path + str(i) + '.jpg')

    images = [open(path, 'rb').read() for path in paths]
    current_image = 0

    @staticmethod
    def frames():
        while True:
            time.sleep(0.5)
            Camera.current_image = (Camera.current_image + 1) % 10
            yield Camera.images[Camera.current_image]
