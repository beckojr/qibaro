from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

index = Blueprint('index', __name__, template_folder='templates', static_folder='static')


@index.route('/', defaults={'page':'index'})
@index.route('/<page>')
def index(page):
    return "Hello world!";
