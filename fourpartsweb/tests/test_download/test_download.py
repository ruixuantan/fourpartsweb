import pytest
import requests

from config import settings
from fourpartsweb.tests.conftest import app

URL = '/api/v1/download/'


def test_render(app):
    """Tests if view for download is rendered.
    """
    response = app.get('/download/')
    assert response.status_code == 200


def test_render_api(app):
    """Tests if api is rendered.
    """
    response = app.get(URL)
    assert response.status_code == 405


def test_post_download(app):
    response = app.post(URL, json={'key': 'wrong key'})
    assert response.status_code == 401

    response = app.post(URL, json={'key': settings.SECRET_KEY})
    assert response.status_code == 200


def test_download_sample(app):
    """Checks if the sample can be downloaded.
    """
    response = app.get('/download/sample/')
    assert response.status_code == 200
