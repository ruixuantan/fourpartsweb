from flask import Blueprint, render_template


index = Blueprint('index', __name__, template_folder='templates')


@index.route('/')
def home():
    return render_template('index/index.html')
