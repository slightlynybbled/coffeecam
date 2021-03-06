import io
import time
import picamera

from coffeecam.base_camera import BaseCamera
from coffeecam.config import FRAME_RATE, RESOLUTION


class Camera(BaseCamera):

    @staticmethod
    def frames():

        with picamera.PiCamera(
                resolution=RESOLUTION, framerate=FRAME_RATE) as camera:
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(
                    stream, 'jpeg',
                    use_video_port=True):

                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
