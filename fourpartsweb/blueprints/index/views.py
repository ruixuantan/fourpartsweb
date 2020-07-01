import os
from flask import Blueprint, render_template, send_from_directory


index = Blueprint('index', __name__, template_folder='templates')


@index.route('/')
def home():
    return render_template('index/home.html')
