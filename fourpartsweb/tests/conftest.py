import pytest

from config import settings
from fourpartsweb.app import create_app
from fourpartsweb.extensions import db as _db


@pytest.fixture
def app():
    db_uri = '{0}_test'.format(settings.SQLALCHEMY_DATABASE_URI)
    params = {
        'DEBUG': False,
        'TESTING': True,
        'SECRET_KEY': settings.SECRET_KEY,
        'SQLALCHEMY_DATABASE_URI': db_uri,
        'MIDISTORE_PATH': settings.MIDISTORE_PATH,
        'PARALLEL_RESULTS_PATH': settings.PARALLEL_RESULTS_PATH,
        'CHORD_RESULTS_PATH': settings.CHORD_RESULTS_PATH
    }

    _app = create_app(settings_override=params)

    ctx = _app.app_context()
    ctx.push()

    yield _app.test_client()

    ctx.pop()
