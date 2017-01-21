from flask import Blueprint, render_template, abort, redirect, request, current_app, url_for, flash
from jinja2 import TemplateNotFound
from app.models import Utilisateur
from ..models import bcrypt, login_manager, LoginForm, RegistrationForm

signing_b = Blueprint('signing', __name__,
                                template_folder='templates',
                                static_folder='static_s')

# Tells to Flask how to load a user given his e-mail
@login_manager.user_loader
def load_user(email):
    return Utilisateur.query.filter(Utilisateur.email == email)

@signing_b.route('/signin/', methods=['GET', 'POST'])
def signin():
    login = LoginForm()
    if login.validate_on_submit():
        print "Input validated"

    else:
        print "Input not validated"

    return render_template('/signin.html', form=login)
    # if request.method == 'GET':
    #     return render_template('/signin.html')
    # elif request.method == 'POST':
    #




@signing_b.route('/signup/', methods=['GET','POST'])
def signup():
    registration = RegistrationForm()
    return render_template('signup.html', form = registration)
