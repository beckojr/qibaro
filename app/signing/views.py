from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

signing_b = Blueprint('signing', __name__,
                                template_folder='templates',
                                static_folder='static_i')

@signing_b.route('/signing/signin')
def signin():
    return render_template('/signin.html')

@signing_b.route('/signup')
def signup():
    return render_template('signup.html')
