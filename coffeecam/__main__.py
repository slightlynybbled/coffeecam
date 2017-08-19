import logging
import os
import datetime

import flask
import picamera
from waitress import serve

from coffeecam.config import *
from coffeecam.util import md5
from coffeecam import create_app

app = create_app()


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


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


def main():
    serve(app, host='0.0.0.0', port=80)
    #app.run(host='0.0.0.0', port=80, debug=True)