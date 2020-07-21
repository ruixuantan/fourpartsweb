import os
from flask import Blueprint, render_template, send_from_directory, current_app


download = Blueprint('download', __name__, template_folder='templates')


@download.route('/download/')
def download_all():
    return render_template('download/download_page.html')


@download.route('/download/sample/')
def download_sample():
    try: 
        return send_from_directory('static/sample/',
                                   'chorale_F.zip', 
                                   as_attachment=True)
    except:
        return jsonify({'error': 'sample files not available'}), 500
