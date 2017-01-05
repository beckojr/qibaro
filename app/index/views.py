from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

index_b = Blueprint('index', __name__, template_folder='templates', static_folder='static')

@index_b.route('/index/')
def index():
    return render_template('index.html')
