import os


DEBUG = True

SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'insecurekeydev'

STORE_PATH = 'fourpartsweb/storage/'
MIDISTORE_PATH = STORE_PATH + 'midifiles/'
PARALLEL_RESULTS_PATH = STORE_PATH + 'parallel_results/'
CHORD_RESULTS_PATH = STORE_PATH + 'chord_results/'

db_uri = 'postgresql://{0}:{1}@postgres:5432/{2}'.format(os.environ['POSTGRES_USER'],
                                                         os.environ['POSTGRES_PASSWORD'],
                                                         os.environ['POSTGRES_DB'])
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Celery.
REDIS_PASSWORD = 'passworddev'
CELERY_BROKER_URL = 'redis://:{}@redis:6379/0'.format(REDIS_PASSWORD)
CELERY_RESULT_BACKEND = 'redis://:{}@redis:6379/0'.format(REDIS_PASSWORD)
CELERY_REDIS_MAX_CONNECTIONS = 5
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    # Executes every 10s
    'clean_db-every-10s': {
        'task': 'clean_db',
        'schedule': 10
    }
}
