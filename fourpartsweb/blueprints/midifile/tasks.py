from os.path import isfile
from flask import current_app
from celery.utils.log import get_task_logger

from fourpartsweb.app import create_celery_app
from fourpartsweb.blueprints.midifile.models import Midifile
from fourpartsweb.extensions import db
from utils import delete_file, generate_results

celery = create_celery_app()
logger = get_task_logger(__name__)


def _delete_files(f):
    """Deletes all files associated with `f` and removes it from db.

    Parameters
    ----------
    f : Midifile
        The associated entry in db.
    """

    delete_file(current_app.config['MIDISTORE_PATH'] + f.midi_string)
    delete_file(current_app.config['PARALLEL_RESULTS_PATH'] + f.parallels_string)
    delete_file(current_app.config['CHORD_RESULTS_PATH'] + f.chords_string)

    db.session.delete(f)
    db.session.commit()
    logger.info("{} deleted".format(f))


@celery.task(name="clean_db")
def clean_db():
    """Every month, iterate through the database and
    check if all files are present. If not, recreate the csv files.
    If this cannot be done, delete the database entry and all associated files.
    """

    files = Midifile.query.all()
    for f in files:

        if not isfile(current_app.config['MIDISTORE_PATH'] + f.midi_string):
            _delete_files(f)

        if not (isfile(current_app.config['PARALLEL_RESULTS_PATH'] + f.parallels_string) and
                isfile(current_app.config['CHORD_RESULTS_PATH'] + f.chords_string)):

            if generate_results(current_app.config['MIDISTORE_PATH'] + f.midi_string,
                                current_app.config['PARALLEL_RESULTS_PATH'] + f.parallels_string,
                                current_app.config['CHORD_RESULTS_PATH'] + f.chords_string):

                logger.info("{} recreated".format(f))

            else:
                _delete_files(f)

    logger.info("DB CLEANED")
