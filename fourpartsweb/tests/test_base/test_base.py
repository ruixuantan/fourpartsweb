import pytest
import requests
from os.path import isdir

from config import settings
from fourpartsweb.tests.conftest import app


def test_render(app):
    response = app.get('/')
    assert response.status_code == 200


def test_storage(app):
    """Checks if the storage folders are initialised.
    """

    assert isdir(settings.MIDISTORE_PATH) and \
           isdir(settings.PARALLEL_RESULTS_PATH) and \
           isdir(settings.CHORD_RESULTS_PATH)
