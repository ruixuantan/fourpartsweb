import pytest
import requests

from fourpartsweb.tests.conftest import app


def test_render(app):
    response = app.get('/')
    assert response.status_code == 200


def test_no_input(app):

    response = app.post('/',
                        data={})
    assert response.status_code != 200
