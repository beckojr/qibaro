from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

admin_b = Blueprint('admin', __name__,
                    template_folder='templates',
                    static_folder='static_ad')
