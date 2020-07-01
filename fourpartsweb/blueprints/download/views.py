import os
from flask import Blueprint, send_from_directory


download = Blueprint('download', __name__)


@download.route('/download/<path:filename>')
def download_page(filename):
    try:
        return send_from_directory("storage/results/", filename, as_attachment=True)
    except FileNotFoundError:
        return 404