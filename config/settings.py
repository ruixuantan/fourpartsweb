import os


DEBUG = True

SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'insecurekeydev'

MIDIFILES = 'fourpartsweb/storage/midifiles/'
RESULTFILES = 'fourpartsweb/storage/results/'

db_uri = 'postgresql://{0}:{1}@postgres:5432/{2}'.format(os.environ['POSTGRES_USER'],
                                                         os.environ['POSTGRES_PASSWORD'],
                                                         os.environ['POSTGRES_DB'])
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False