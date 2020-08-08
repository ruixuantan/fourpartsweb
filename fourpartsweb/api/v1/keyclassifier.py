import os

from flask import jsonify, request, current_app
from werkzeug.utils import secure_filename
from fourpartsweb.api.v1 import V1FlaskView
from utils import delete_file


class KeyclassifierView(V1FlaskView):
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
        filedir = current_app.config['MIDISTORE_PATH'] + filename_mid
        posted_file.save(os.path.join(filedir))

        key = current_app.config['KEY_CLASSIFIER'].predict_midi(filedir)[0]
        delete_file(filedir)

        response = jsonify({'key': key})
        return response, 200
