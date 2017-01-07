from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

index_b = Blueprint('index', __name__,
                    template_folder='templates',
                    static_folder='static_i')

@index_b.route('/')
def index():
    return render_template('index.html')
