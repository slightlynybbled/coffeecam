import flask

from coffeecam.version import __version__
from coffeecam.config import *


def create_app():
    app = flask.Flask(__name__, template_folder='templates')

    from coffeecam.views import pages

    app.register_blueprint(pages)

    return app
