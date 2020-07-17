DEBUG = False

SERVER_NAME = 'fourparts.herokuapp.com'
SECRET_KEY = 'insecurekeydev'

MIDISTORE_PATH = 'fourpartsweb/storage/midifiles/'
RESULTSTORE_PATH = 'fourpartsweb/storage/results/'

# USER
# PASSWORD
# DB

db_uri = 'postgres://pddovxouxdhfts:8fc7ca66a729d2fb2f58efe2b2d8e83abe055ec5be827edc0677983905f879e0@ec2-54-159-138-67.compute-1.amazonaws.com:5432/dc3cihr5l0c5ao'

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
