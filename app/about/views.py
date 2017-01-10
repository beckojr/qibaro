from flask import Blueprint, render_template, abort, current_app
from jinja2 import TemplateNotFound

about_b = Blueprint('about', __name__,
                    template_folder='templates',
                    static_folder='static_ab')
