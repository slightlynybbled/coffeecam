import logging
import os

import flask
from waitress import serve

from coffeecam.util import md5
from coffeecam import create_app
from coffeecam.config import PORT


app = create_app()


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


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
    serve(app, host='0.0.0.0', port=PORT)
    #app.run(host='0.0.0.0', port=PORT, debug=True)
