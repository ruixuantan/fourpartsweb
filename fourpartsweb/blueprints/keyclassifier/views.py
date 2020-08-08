from flask import Blueprint, render_template


key_classifier = Blueprint('key_classifier', __name__, template_folder='templates')


@key_classifier.route('/keyclassifier/')
def key_classifier_page():
    return render_template('key_classifier/index.html')
