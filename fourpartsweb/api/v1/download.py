import time
import shutil
import os

from io import BytesIO
import zipfile

from fourpartsweb.api.v1 import V1FlaskView
from flask import current_app, jsonify, request, Response, send_from_directory, send_file


class DownloadView(V1FlaskView):
    def post(self):
        """Returns all storage files in a zip file.
        """
        data = request.get_json()

        if 'key' not in data:
            return jsonify({'error': 'wrong request'}), 400

        if current_app.config['SECRET_KEY'] != data['key']:
            return jsonify({'error': 'invalid key'}), 401

        print("SUCCESS NOWNOWNOW")

        timestr = time.strftime("%Y%m%d-%H%M%S")

        filename = "storage_files"
        file_path = 'storage/results/'

        shutil.make_archive('fourpartsweb/storage/' + filename,
                            'zip',
                            'fourpartsweb/storage/')
        
        return send_from_directory("storage/", filename + ".zip", as_attachment=True)


        # timestr = time.strftime("%Y%m%d-%H%M%S")
        # fileName = "my_data_dump_{}.zip".format(timestr)
        # memory_file = BytesIO()
        # file_path = 'storage/midifiles/'
        # with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        #     for root, dirs, files in os.walk(file_path):
        #                 for file in files:
        #                         zipf.write(os.path.join(root, file))
        # memory_file.seek(0)
        # return send_file(memory_file,
        #                 attachment_filename=fileName,
        #                 as_attachment=True)