from flask import Blueprint, render_template


pitch_class_set = Blueprint('pitch_class_set', __name__, template_folder='templates')


@pitch_class_set.route('/pitchclassset/')
def pitch_class_set_page():
    return render_template('pitch_class_set/pitch_class_set.html')
