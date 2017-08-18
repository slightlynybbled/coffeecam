import logging
import os
import hashlib
import datetime

import flask
import picamera
from waitress import serve


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

cam = picamera.PiCamera()
last_pic_time = datetime.datetime.now()

app = flask.Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.jinja2')


@app.route('/about')
def about():
    return flask.render_template('about.jinja2')


@app.route('/take_pic', methods=['POST'])
def take_pic():
    global last_pic_time

    logger.debug('requesting new pic')
    now = datetime.datetime.now()

    cam_path = '/home/jason/coffeecam/static/ram/live.jpg'
    if (now - last_pic_time) > datetime.timedelta(seconds=2):
        cam.capture(cam_path)
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

serve(app, host='0.0.0.0', port=80)
#app.run(host='0.0.0.0', port=80, debug=True)