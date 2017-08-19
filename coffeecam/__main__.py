import logging
import os
import hashlib
import datetime

import flask
import picamera
from waitress import serve
import humanize

from coffeecam.config import *


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


last_pic_time = datetime.datetime.now()

cam = picamera.PiCamera()
cam.capture(cam_path)

users = set()
user_logins = dict()
havent_logged_in_since = dict()

app = flask.Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
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


@app.route('/about')
def about():
    return flask.render_template('about.jinja2')


@app.route('/set_time', methods=['POST'])
def set_time():
    date = int(int(flask.request.form['date'])/1000)

    dt = datetime.datetime.fromtimestamp(date)
    now = datetime.datetime.now()

    if dt < now + datetime.timedelta(hours=1) > dt or dt > now - datetime.timedelta(hours=1):
        logger.info('time already set, leaving it alone')
    else:
        logger.warning('setting time to {}'.format(dt))

        new_dt = dt.strftime('%m/%d/%y %H:%M:%S')
        os.system('hwclock --set --date="{}"'.format(new_dt))

    return '', 204


@app.route('/take_pic', methods=['POST'])
def take_pic():
    global last_pic_time

    logger.debug('requesting new pic')
    now = datetime.datetime.now()

    if (now - last_pic_time) > datetime.timedelta(seconds=2):

        logger.info('new pic complete!')
        last_pic_time = datetime.datetime.now()

    else:
        logger.warning('old pic is still fresh, skipping')

    src = flask.url_for('static', filename='ram/live.jpg') + '?src=' + md5(cam_path)

    return flask.jsonify({'src': src})


@app.context_processor
def override_url_for():
    return dict(url_for=hashed_url_for)


def hashed_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['hash'] = md5(file_path)

    return flask.url_for(endpoint, **values)


def md5(fname):
    hash_md5 = hashlib.md5()
    try:
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except FileNotFoundError:
        return '0'


def find_most_logins(user_logins):
    u = list(user_logins.keys())[0]

    if len(u) == 0:
        return '-', '-'

    l = user_logins.get(u)

    for user, logins in user_logins.items():
        if logins > l:
            u = user
            l = logins

    return u, l


def main():
    serve(app, host='0.0.0.0', port=80)
    #app.run(host='0.0.0.0', port=80, debug=True)