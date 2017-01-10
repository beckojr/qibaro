from flask import Blueprint, render_template, abort, current_app
from jinja2 import TemplateNotFound

profile_b = Blueprint('profile', __name__,
                        template_folder='templates',
                        static_folder='static_p')
