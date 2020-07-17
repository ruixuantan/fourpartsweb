DEBUG = False

SERVER_NAME = 'fourparts.herokuapp.com'
SECRET_KEY = 'insecurekeydev'

MIDISTORE_PATH = 'fourpartsweb/storage/midifiles/'
RESULTSTORE_PATH = 'fourpartsweb/storage/results/'

# USER
# PASSWORD
# DB

db_uri = 'insert heroku key here'

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
