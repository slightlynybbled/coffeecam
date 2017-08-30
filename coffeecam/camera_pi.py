import io
import time
import picamera
from coffeecam.base_camera import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def frames():
        # todo: make resolution and frame rate settable via config file

        with picamera.PiCamera(resolution='720p') as camera:
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(
                    stream, 'jpeg',
                    use_video_port=True):
                time.sleep(0.5)

                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
