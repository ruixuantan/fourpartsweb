DEBUG = False

SERVER_NAME = 'fourparts.herokuapp.com'
SECRET_KEY = 'insecurekeydev'

# USER
# PASSWORD
# DB

db_uri = 'postgresql://{0}:{1}@postgres:5432/{2}'.format('fourparts',
                                                         'fourpartspassword',
                                                         'fourparts')
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
