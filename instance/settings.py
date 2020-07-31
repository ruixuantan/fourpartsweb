from celery.schedules import crontab
import os


DEBUG = False

SERVER_NAME = 'fourparts.herokuapp.com'
SECRET_KEY = os.environ['PRODUCTION_SECRET_KEY']

STORE_PATH = 'fourpartsweb/storage/'
MIDISTORE_PATH = STORE_PATH + 'midifiles/'
PARALLEL_RESULTS_PATH = STORE_PATH + 'parallel_results/'
CHORD_RESULTS_PATH = STORE_PATH + 'chord_results/'

# USER
# PASSWORD
# DB

db_uri = 'insert heroku key here'

SQLALCHEMY_DATABASE_URI = os.environ['PRODUCTION_DB_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Celery.
REDIS_PASSWORD = 'insert secure redis password here'
CELERY_BROKER_URL = 'redis://:{}@redis:6379/0'.format(REDIS_PASSWORD)
CELERY_RESULT_BACKEND = 'redis://:{}@redis:6379/0'.format(REDIS_PASSWORD)
CELERY_REDIS_MAX_CONNECTIONS = 5
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'clean_db-every-month': {
        'task': 'clean_db',
        'schedule': crontab(0, 0, day_of_month='1')
    }
}
