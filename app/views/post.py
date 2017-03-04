#coding=utf-8
from flask import Blueprint, render_template, abort, flash, redirect, url_for, session
from jinja2 import TemplateNotFound
from flask_login import logout_user
from flask_login import login_required

post = Blueprint('post_b', __name__)

@post.route('/post/')
@login_required
def publish():
    return render_template('post/editor.html')
