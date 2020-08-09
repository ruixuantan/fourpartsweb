import pytest
import requests

from fourpartsweb.tests.conftest import app

URL = '/api/v1/keyclassifier/'


def test_render_api(app):
    response = app.get(URL)
    assert response.status_code == 405
