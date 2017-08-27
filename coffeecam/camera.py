from datetime import datetime, timedelta
from io import BytesIO
import picamera
from time import time
import os


class Camera:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = str(dir_path) + '/static/img/'
        self.frames = [open(dir_path + f + '.jpg', 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        return self.frames[int(time()) % 3]


'''
class Camera:
    def __init__(self, framerate=1.0, test=False):
        if framerate > 0.0:
            self.interval = 1/framerate
        else:
            self.interval = 0

        self.test = test

        if not self.test:
            self.camera = picamera.PiCamera()

        self.last_snapshot = datetime.now()
        self.stream = BytesIO()

    def snapshot(self):
        if self.last_snapshot + timedelta(seconds=self.interval) > datetime.now():
            self.stream.truncate()
            self.camera.capture(self.stream, 'jpeg')
            self.last_snapshot = datetime.now()

    def get_frame(self):
        self.stream.seek(0)
        yield self.stream.read()
        '''



