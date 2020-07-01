# Fourparts Web #
The deployment of the Fourparts package on a site. \
Link to site: 

To build project:
```console
$ docker-compose build
$ docker-compose up postgres
```
Local build is on https://localhost:8000

## Notes ##
Currently, to avoid duplicates of filenames, when the midi file is uploaded, 
a python hash is generated from the concatenated string of the current datetime object
and original midi filename. This will then be used as the new filename of both midi and csv files.

## Extension ##
Build a background job that checks the database every now and then.
It checks if the files in the database exists.
If the files do not exist (or 1 is missing), the job deletes the
entry in the database, both csv and midi files.