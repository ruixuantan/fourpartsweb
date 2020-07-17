# Fourparts Web #
The deployment of the Fourparts package on a site. \
Link to site: https://fourparts.herokuapp.com

To build project:
```
$ docker-compose build
$ docker-compose up postgres
```

To configure postgres, open up a new terminal while the image is running and enter:
```
$ docker-compose exec server python3
Python
>>> from fourpartsweb.extensions import db
>>> from fourpartsweb.app import create_app
>>> app = create_app()
>>> db.app = app
>>> db.drop_all()
>>> db.create_all()
```

Local build is on https://localhost:8000

To run tests:
```
$ docker-compose exec server pytest
```

## Deployment ##
### Heroku ###
Ensure set up of initial app and postgres add-on in Heroku. Add the heroku postgres db uri to instance.settings.py file. 

In app.py, change `app.config.from_object('config.settings')` to `app.config.from_object('instance.settings')`

In Dockerfile and docker-compose.yml, change the command to `gunicorn "fourpartsweb.app:create_app()"`

## Notes ##
Currently, to avoid duplicates of filenames, when the midi file is uploaded, 
a python hash is generated from the concatenated string of the current datetime object
and original midi filename. This will then be used as the new filename of both midi and csv files.

## Extension ##
1. Build a background job that checks the database every now and then.
It checks if the files in the database exists.
If the files do not exist (or 1 is missing), the job deletes the
entry in the database and both csv and midi files.

2. Build a CLI package that abstracts away the need of manually setting up the database.