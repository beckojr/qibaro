# coding=utf-8

from flask import Blueprint, render_template, abort, redirect, request as req, current_app, url_for
from flask_login import login_user
from jinja2 import TemplateNotFound
from app.models import Utilisateur
from ..models import bcrypt, login_manager, LoginForm, RegistrationForm

signing = Blueprint('signing_b', __name__)

# Tells to Flask how to load a user given his e-mail
@login_manager.user_loader
def load_user(email):
    return Utilisateur.query.filter(Utilisateur.email == email).first()

@signing.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if req.method == "POST":
        if form.validate_on_submit():
            utilisateur = load_user(form.email.data)
            login_user(utilisateur)
            return redirect(req.args.get("next") or url_for('feed_b.index'))
    return render_template('signing/signin.html', form = form)




@signing.route('/signup/', methods=['GET','POST'])
def signup():
    form = RegistrationForm()

    if req.method == "POST":
        if form.validate_on_submit():
            utilisateur = Utilisateur()

            # form.populate_obj(utilisateur)
            utilisateur.prenom = form.prenom.data
            utilisateur.nom = form.nom.data
            utilisateur.email = form.email.data
            utilisateur.motdepasse(form.passwd.data)
            utilisateur.save()
            login_user(utilisateur)
            return redirect(url_for('feed_b.index'))
    return render_template('signing/signup.html', form = form)
