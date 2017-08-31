import datetime
import flask
import logging
import os

from coffeecam import *
from coffeecam.camera_pi import Camera
from coffeecam.config import HOST_NAME

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

pages = flask.Blueprint('pages', __name__)

users = set()
last_checkin = dict()


@pages.route('/')
@pages.route('/index')
def index():
    user_id = flask.request.remote_addr.split('.')[-1]

    return flask.render_template(
        'index.jinja2',
        user_id=user_id,
        show_stats=SHOW_STATS,
        host=HOST_NAME
    )


@pages.route('/about')
def about():
    return flask.render_template('about.jinja2', host=HOST_NAME)


@pages.route('/set_time', methods=['POST'])
def set_time():
    date = int(int(flask.request.form['date'])/1000)

    dt = datetime.datetime.fromtimestamp(date)
    now = datetime.datetime.now()

    if dt < now + datetime.timedelta(hours=1) > dt or dt > now - datetime.timedelta(hours=1):
        logger.info('time set, leaving it alone')
    else:
        logger.warning('setting time to {}'.format(dt))

        new_dt = dt.strftime('%m/%d/%y %H:%M:%S')
        os.system('hwclock --set --date="{}"'.format(new_dt))

    return '', 200


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@pages.route('/video_feed')
def video_feed():
    return flask.Response(
        gen(Camera()),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


@pages.route('/users', methods=['POST'])
def users():
    user_id = flask.request.remote_addr.split('.')[-1]

    last_checkin[user_id] = datetime.datetime.now()

    current_users = []
    num_of_users = 0
    for user, dt_last in last_checkin.items():
        if dt_last > (datetime.datetime.now() - datetime.timedelta(seconds=10)):
            current_users.append(user)
        num_of_users += 1

    return flask.jsonify(
        {'current_users': current_users, 'num_of_users': num_of_users}
    )
