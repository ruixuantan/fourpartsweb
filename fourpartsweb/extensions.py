from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


debug_toolbar = DebugToolbarExtension()
db = SQLAlchemy()
marshmallow = Marshmallow()
