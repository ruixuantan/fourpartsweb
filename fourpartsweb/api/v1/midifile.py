from datetime import datetime
from flask import jsonify, request, Response
import os
from werkzeug.utils import secure_filename

import fourparts as fp
import pandas as pd

from fourpartsweb.api.v1 import V1FlaskView
from fourpartsweb.blueprints.midifile.models import Midifile
from fourpartsweb.extensions import db


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
        hashed_filename = str(hash(filename_mid[:-4] + str(datetime.now())))
        hashed_filename_mid = hashed_filename + '.mid'
        hashed_filename_csv = hashed_filename + '.csv'

        save_path = "fourpartsweb/storage/"
        midi_path = save_path + "midifiles/" + hashed_filename_mid
        csv_path = save_path + "results/" + hashed_filename_csv

        # save midifile
        posted_file.save(os.path.join(save_path + "midifiles/", hashed_filename_mid))

        try:
            df = fp.midi_to_df(midi_path)
            chords = fp.get_chord_progression(df)
            result = fp.ChordProgression(chords).check_parallels()
            pd.DataFrame(result).to_csv(csv_path)

        except:
            os.remove(midi_path)
            response = jsonify({'error': 'an invalid midi file was uploaded'})
            return response, 400

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
            response = jsonify({'error': 'an internal server error occured.'})
            return response, 500

        return jsonify(hashed_filename_csv), 200
