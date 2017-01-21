from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask_login import login_required

index_b = Blueprint('index', __name__,
                    template_folder='templates',
                    static_folder='static_i')

@index_b.route('/')
@login_required
def index():
    return render_template('index.html')
