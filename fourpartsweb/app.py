from flask import Flask
from celery import Celery
import os

from key_classifier.KeyClassifier import initialise_key_classifier

from fourpartsweb.blueprints.index import index
from fourpartsweb.blueprints.download import download
from fourpartsweb.blueprints.pitchclassset import pitch_class_set
from fourpartsweb.api.v1.midifile import MidifileView
from fourpartsweb.api.v1.download import DownloadView
from fourpartsweb.api.v1.pitchclass import PitchclassView
from fourpartsweb.api.v1.keyclassifier import KeyclassifierView
from fourpartsweb.extensions import (
    debug_toolbar,
    db,
    marshmallow
)

CELERY_TASK_LIST = [
    'fourpartsweb.blueprints.midifile.tasks'
]


def create_celery_app(app=None):
    app = app or create_app()

    celery = Celery(app.import_name,
                    broker=app.config['CELERY_BROKER_URL'],
                    include=CELERY_TASK_LIST
                    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(settings_override=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')

    if settings_override:
        app.config.update(settings_override)

    _create_storage_folders(app)

    app.register_blueprint(index)
    app.register_blueprint(download)
    app.register_blueprint(pitch_class_set)

    extensions(app)

    MidifileView.register(app)
    DownloadView.register(app)
    PitchclassView.register(app)
    KeyclassifierView.register(app)

    classifier = initialise_key_classifier()

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
