#coding=utf-8
from flask import Blueprint, render_template, abort, flash, redirect, url_for, session
from jinja2 import TemplateNotFound
from flask_login import logout_user
from flask_login import login_required

index_b = Blueprint('index', __name__,
                    template_folder='templates',
                    static_folder='static_i')

@index_b.route('/')
@login_required
def index():
    return render_template('index.html')

@index_b.route('/logout/')
@login_required
def logout():
    """Loging out function handler"""
    logout_user()
    flash("Vous avez été déconnecté avec succès")
    return redirect(url_for('index.index'))
