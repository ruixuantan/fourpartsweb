import pytest
import requests

from fourpartsweb.tests.conftest import app

URL = '/api/v1/pitchclass/'


def test_render(app):
    response = app.get('/pitchclassset/')
    assert response.status_code == 200


def test_render_api(app):
    response = app.get(URL)
    assert response.status_code == 405


def test_pitch_class_set(app):
    response = app.post(URL, json={'notes': [0, 1, 2, 3]})
    assert response.status_code == 200

    response = app.post(URL, json={'notes': [1]})
    assert response.status_code == 200

    response = app.post(URL, json={'notes': []})
    assert response.status_code == 200

    response = app.post(URL, json={'notes': [0, 1, 2, 3, 4, 5, 6, 7]})
    assert response.status_code == 200
