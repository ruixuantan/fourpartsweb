DEBUG = False

SERVER_NAME = 'fourparts.herokuapp.com'
SECRET_KEY = 'insert secure key here'

STORE_PATH = 'fourpartsweb/storage/'
MIDISTORE_PATH = STORE_PATH + 'midifiles/'
PARALLEL_RESULTS_PATH = STORE_PATH + 'parallel_results/'
CHORD_RESULTS_PATH = STORE_PATH + 'chord_results/'

# USER
# PASSWORD
# DB

db_uri = 'insert heroku key here'

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
