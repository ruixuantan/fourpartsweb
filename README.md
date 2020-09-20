# FourPartsWeb
The deployment of [FourParts](https://github.com/ruixuantan/FourParts) on a [flask app](https://fourparts.herokuapp.com).

### ToC
1. [Flask Setup](#flask-setup)
1. [Flask CLI](#flask-cli)
1. [Deployment](#deployment)
1. [Streamlit](#streamlit)
1. [Misc](#misc)

## Flask Setup
To build project:

Create a `.env` file in the root of the directory and configure it:
```
COMPOSE_PROJECT_NAME=fourpartsweb
POSTGRES_USER=insertuser
POSTGRES_PASSWORD=insertpassword
POSTGRES_DB=insertdb
PYTHONUNBUFFERED=true
```

Then, run:
```
$ python3 setup.py bdist_wheel
$ docker-compose up --build
```

To configure postgres, open up a new terminal while the container is running and enter:
```
$ docker-compose run server fourpartsweb db init
```

Local build is on http://localhost:8000 \
Midi samples can be found [here](https://github.com/ruixuantan/FourParts/tree/master/samples)

## Flask CLI
To run tests and flake8:
```
$ docker-compose exec server pytest
$ docker-compose exec server flake8
```

To delete storage files:
```
$ docker-compose run server fourpartsweb storage del-storage
```

## Deployment
### Heroku
Ensure set up of initial app and postgres add-on in Heroku.
Create an `instance/settings.py` file, similar to that in `config/settings.py`, but with the actual production keys.

In app.py, change `app.config.from_object('config.settings')` to `app.config.from_object('instance.settings')`

In Dockerfile and docker-compose.yml, change the command to `gunicorn "fourpartsweb.app:create_app()"`

## Streamlit
The [Streamlit](https://www.streamlit.io) package is used to train the KeyClassifier model.

A python venv has to be setup first, along with the python packages.
```
python3 -m venv env
pip install -r requirements.txt
```

To start the streamlit app, run:
```
streamlit run streamlit_app/key_classifier_app.py
```
Build will be on http://localhost:8501.

## Misc
### Notes
Currently, to avoid duplicates of filenames, when the midi file is uploaded, a python hash is generated from the concatenated string of the current datetime object and original midi filename. This will then be used as the new filename of both midi and csv files.

### Next Steps
1. Write tests for CLI scripts and celery.
2. Configure webpack to precompile jquery functions or refactor to another javascript library (React).