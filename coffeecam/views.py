import datetime
import humanize
import flask
import logging
import os

import picamera

from coffeecam.util import find_most_logins, md5
from coffeecam import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

pages = flask.Blueprint('pages', __name__)

# use these to keep local stats
users = set()
user_logins = dict()
havent_logged_in_since = dict()


last_pic_time = datetime.datetime.now()

cam = picamera.PiCamera()
cam.capture(os.path.join(MEDIA_DIR, MEDIA_NAME))


@pages.route('/')
@pages.route('/index')
def index():
    user_id = flask.request.remote_addr.split('.')[-1]
    users.add(user_id)

    if user_id not in user_logins.keys():
        user_logins[user_id] = 1
    else:
        user_logins[user_id] += 1

    last_logged_in = havent_logged_in_since.get(user_id)
    if last_logged_in is not None:
        td = datetime.datetime.now() - last_logged_in
        last_logged_in = humanize.naturaldelta(td)

    else:
        last_logged_in = 'never'

    havent_logged_in_since[user_id] = datetime.datetime.now()

    return flask.render_template(
        'index.jinja2',
        users=len(users),
        your_logins=user_logins[user_id],
        user_logins=find_most_logins(user_logins),
        user_id=user_id,
        last_login=last_logged_in,
        show_stats=show_stats
    )


@pages.route('/about')
def about():
    return flask.render_template('about.jinja2')


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


@pages.route('/take_pic', methods=['POST'])
def take_pic():
    global last_pic_time

    now = datetime.datetime.now()

    if (now - last_pic_time) > datetime.timedelta(seconds=2):
        last_pic_time = datetime.datetime.now()
        logger.debug('stale image detected')
        cam.capture(os.path.join(MEDIA_DIR, MEDIA_NAME))

    path = os.path.join(MEDIA_DIR, MEDIA_NAME)
    src = MEDIA_URL + MEDIA_NAME + '?' + md5(path)

    return flask.jsonify({'src': src})
