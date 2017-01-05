from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

profile = Blueprint('profile', __name__, template_folder='templates', static_folder='static')
