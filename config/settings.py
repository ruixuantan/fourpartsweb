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
