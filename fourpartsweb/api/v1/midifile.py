from flask import current_app, jsonify, request, send_file
from io import BytesIO
import os
from werkzeug.utils import secure_filename
from zipfile import ZipFile

from fourpartsweb.api.v1 import V1FlaskView
from fourpartsweb.blueprints.midifile.models import Midifile
from fourpartsweb.extensions import db
from utils import get_time_string, delete_file, generate_results, FileCollection


def _db_commit(file_collection):
    """Saves string of midi file and generated csv files into db.

    Returns
    -------
    bool
        Returns True if there are no errors in the saving.
    """

    try:
        # save into db
        midifile = Midifile()
        midifile.midi_string = file_collection.midifile
        midifile.parallels_string = file_collection.parallels_result
        midifile.chords_string = file_collection.chords_result
        db.session.add(midifile)
        db.session.commit()

    except Exception:
        delete_file(file_collection.midi_path)
        delete_file(file_collection.parallels_path)
        delete_file(file_collection.chords_path)
        return False

    return True


def _zip_results(file_collection):
    """Zips the parallel and chord analysis csv files.
    """

    memory_file = BytesIO()

    with ZipFile(memory_file, 'w') as zipf:
        zipf.write(file_collection.parallels_path,
                   'parallels.csv')
        zipf.write(file_collection.chords_path,
                   'chords.csv')

    memory_file.seek(0)
    return memory_file


class MidifileView(V1FlaskView):
    def post(self):
        if 'file' not in request.files:
            response = jsonify({'error': 'file not uploaded'})
            return response, 400

        posted_file = request.files['file']
        filename_mid = posted_file.filename

        if filename_mid[-4:] != '.mid':
            response = jsonify({'error': 'a non midi file was uploaded'})
            return response, 400

        filename_mid = secure_filename(filename_mid)
        file_collection = FileCollection.generate_file_collection(filename_mid,
                                                                  current_app.config['MIDISTORE_PATH'],
                                                                  current_app.config['PARALLEL_RESULTS_PATH'],
                                                                  current_app.config['CHORD_RESULTS_PATH'])
        # save midifile
        posted_file.save(os.path.join(file_collection.midi_path))

        if not generate_results(file_collection.midi_path,
                                file_collection.parallels_path,
                                file_collection.chords_path):
            return jsonify({'error': 'an invalid midi file was uploaded'}), 400

        if not _db_commit(file_collection):
            return jsonify({'error': 'an internal server error occured.'}), 500

        try:
            zip_file = _zip_results(file_collection)
            filename = "results_{}.zip".format(get_time_string())
            return send_file(zip_file,
                             attachment_filename=filename,
                             as_attachment=True)

        except FileNotFoundError:
            return jsonify({'error': 'file is not properly zipped in server.'}), 500
