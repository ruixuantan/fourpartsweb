# Fourparts Web #
The deployment of the Fourparts package (https://github.com/ruixuantan/FourParts) on a site. \
Link to site: https://fourparts.herokuapp.com

To build project:
```
$ python3 setup.py bdist_wheel
$ docker-compose build
$ docker-compose up postgres
```

To configure postgres, open up a new terminal while the container is running and enter:
```
$ docker-compose run server fourpartsweb db init
```

Local build is on http://localhost:8000 \
Midi samples can be found here: https://github.com/ruixuantan/FourParts/tree/master/samples

## CLI ##
To run tests:
```
$ docker-compose exec server pytest
```

To delete storage files:
```
$ docker-compose run server fourpartsweb storage del-storage
```

## Deployment ##
### Heroku ###
Ensure set up of initial app and postgres add-on in Heroku. Add the secret key and heroku postgres db uri to instance.settings.py file. 

In app.py, change `app.config.from_object('config.settings')` to `app.config.from_object('instance.settings')`

In Dockerfile and docker-compose.yml, change the command to `gunicorn "fourpartsweb.app:create_app()"`

## Notes ##
Currently, to avoid duplicates of filenames, when the midi file is uploaded, 
a python hash is generated from the concatenated string of the current datetime object
and original midi filename. This will then be used as the new filename of both midi and csv files.

## Extension ##
1. Build a background job that checks the database every now and then.
It checks if the files in the database exists.
If the files do not exist (or 1 is missing), it deletes the
entry in the database and both csv and midi files.
