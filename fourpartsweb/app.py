from flask import Flask
import os

from fourpartsweb.blueprints.index import index
from fourpartsweb.blueprints.download import download
from fourpartsweb.api.v1.midifile import MidifileView
from fourpartsweb.api.v1.download import DownloadView

from fourpartsweb.extensions import (
    debug_toolbar,
    db,
    marshmallow
)


def create_app(settings_override=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')

    if settings_override:
        app.config.update(settings_override)

    _create_storage_folders(app)

    app.register_blueprint(index)
    app.register_blueprint(download)

    extensions(app)

    MidifileView.register(app)
    DownloadView.register(app)

    return app


def extensions(app):
    debug_toolbar.init_app(app)
    db.init_app(app)
    marshmallow.init_app(app)

    return None


def _create_folder(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def _create_storage_folders(app):
    _create_folder(app.config["MIDISTORE_PATH"])
    _create_folder(app.config["PARALLEL_RESULTS_PATH"])
    _create_folder(app.config["CHORD_RESULTS_PATH"])

