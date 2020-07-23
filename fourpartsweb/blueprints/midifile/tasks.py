import os
from flask import current_app
from celery.utils.log import get_task_logger

from fourpartsweb.app import create_celery_app
from fourpartsweb.blueprints.midifile.models import Midifile
from fourpartsweb.extensions import db
from utils import delete_file

celery = create_celery_app()
logger = get_task_logger(__name__)


def _check_presence(f):
    """Checks if all the files are present
    as represented in the database.

    Parameters
    ----------
    f : Midifile

    Returns
    -------
    bool
        True if all the files are present.
    """

    midi_present = os.path.isfile(current_app.config['MIDISTORE_PATH'] + f.midi_string)
    parallels_present = os.path.isfile(current_app.config['PARALLEL_RESULTS_PATH'] + f.parallels_string)
    chords_present = os.path.isfile(current_app.config['CHORD_RESULTS_PATH'] + f.chords_string)

    return midi_present and parallels_present and chords_present


def _delete_files(f):
    """Deletes all files associated with `f`.

    Parameters
    ----------
    f : string
        The hashed string of the filename.
        It should not end with a .mid suffix.
    """

    if f[:-4] == '.mid':
        f = f[:-4]

    delete_file(current_app.config['MIDISTORE_PATH'] + f + ".mid")
    delete_file(current_app.config['PARALLEL_RESULTS_PATH'] + f + ".csv")
    delete_file(current_app.config['CHORD_RESULTS_PATH'] + f + ".csv")


@celery.task(name="clean_db")
def clean_db():
    """Every month, iterate through the database and 
    checks if all files are present. If not, delete all
    the database entry and all associated files.
    """
    files = Midifile.query.all()
    for f in files:
        if not _check_presence(f):
            filename = f.midi_string[:-4]
            _delete_files(filename)
            db.session.delete(f)
            db.session.commit()
            logger.info("{} deleted".format(f))

    logger.info("DB CLEANED")
