from flask import Blueprint, render_template, send_from_directory, jsonify


download = Blueprint('download', __name__, template_folder='templates')


@download.route('/download/')
def download_all():
    return render_template('download/index.html')


@download.route('/download/sample/')
def download_sample():
    try:
        return send_from_directory('static/sample/',
                                   'chorale_F.zip',
                                   as_attachment=True)
    except FileNotFoundError:
        return jsonify({'error': 'sample files not available'}), 500
