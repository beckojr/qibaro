#coding=utf-8
from flask import Blueprint, render_template, abort, flash, redirect, url_for, session
from jinja2 import TemplateNotFound
from flask_login import logout_user
from flask_login import login_required

feed = Blueprint('feed_b', __name__)

@feed.route('/')
@login_required
def index():
    return render_template('feed/index.html')


@feed.route('/logout/')
@login_required
def logout():
    """Loging out function handler"""
    logout_user()
    flash("Vous avez été déconnecté avec succès")
    return redirect(url_for('feed_b.index'))
