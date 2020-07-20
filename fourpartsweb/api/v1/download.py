from io import BytesIO
import os
import time
import zipfile

from fourpartsweb.api.v1 import V1FlaskView
from flask import current_app, jsonify, request, send_file


class DownloadView(V1FlaskView):
    def post(self):
        """Returns all storage files in a zip file.
        """
        data = request.get_json()

        if 'key' not in data:
            return jsonify({'error': 'wrong request'}), 400

        if current_app.config['SECRET_KEY'] != data['key']:
            return jsonify({'error': 'invalid key'}), 401

        # python's zipfile library to zip a folder.
        # Does not save the zipped folder.
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = "storage_{0}.zip".format(timestr)
        memory_file = BytesIO()
        file_path = current_app.config['STORE_PATH']
        with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(file_path):
                for file in files:
                    zipf.write(os.path.join(root, file))

        memory_file.seek(0)
        return send_file(memory_file,
                         attachment_filename=filename,
                         as_attachment=True)