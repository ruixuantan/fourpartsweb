from datetime import datetime
from flask import current_app, jsonify, request, send_from_directory
import os
from werkzeug.utils import secure_filename
import fourparts as fp
import pandas as pd

from fourpartsweb.api.v1 import V1FlaskView
from fourpartsweb.blueprints.midifile.models import Midifile
from fourpartsweb.extensions import db


def _generate_hashed_filenames(filename):
    if filename[:-4] == '.mid':
        filename = filename[:-4]

    hashed_filename = str(hash(filename + str(datetime.now())))
    hashed_filename_mid = hashed_filename + '.mid'
    hashed_filename_csv = hashed_filename + '.csv'

    return hashed_filename_mid, hashed_filename_csv


def _generate_results(midi_path, csv_path):
    """Generates results of the analysed midi file.
    """
    df = fp.midi_to_df(midi_path)
    chords = fp.get_chord_progression(df)
    result = fp.ChordProgression(chords).check_parallels()
    pd.DataFrame(result).to_csv(csv_path)


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
        hashed_filename_mid, hashed_filename_csv = _generate_hashed_filenames(filename_mid)

        midi_path = current_app.config["MIDISTORE_PATH"] + hashed_filename_mid
        csv_path = current_app.config["RESULTSTORE_PATH"] + hashed_filename_csv

        # save midifile
        posted_file.save(os.path.join(midi_path))

        try:
            _generate_results(midi_path, csv_path)

        except:
            os.remove(midi_path)
            return jsonify({'error': 'an invalid midi file was uploaded'}), 400

        try:
            # save into db
            midifile = Midifile()
            midifile.midi_string = hashed_filename_mid
            midifile.csv_string = hashed_filename_csv
            db.session.add(midifile)
            db.session.commit()

        except:
            os.remove(midi_path)
            os.remove(csv_path)
            return jsonify({'error': 'an internal server error occured.'}), 500

        return send_from_directory("storage/results/", 
                                    hashed_filename_csv, 
                                    as_attachment=True)
