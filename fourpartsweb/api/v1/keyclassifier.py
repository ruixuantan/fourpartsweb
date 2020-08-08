from flask import jsonify, request, current_app

from fourpartsweb.api.v1 import V1FlaskView


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

        key = current_app.classifier.predict_midi(filename_mid)
        response = jsonify({'key': key})

        return response, 200