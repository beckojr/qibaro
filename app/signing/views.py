# coding=utf-8

from flask import Blueprint, render_template, abort, redirect, request as req, current_app, url_for
from flask_login import login_user
from jinja2 import TemplateNotFound
from app.models import Utilisateur
from ..models import bcrypt, login_manager, LoginForm, RegistrationForm

signing_b = Blueprint('signing', __name__,
                                template_folder='templates',
                                static_folder='static_s')

# Tells to Flask how to load a user given his e-mail
@login_manager.user_loader
def load_user(email):
    return Utilisateur.query.filter(Utilisateur.email == email).first()

@signing_b.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if req.method == "POST":
        if form.validate_on_submit():
            # utilisateur = Utilisateur.query.filter(Utilisateur.email == form.email.data).first()
            utilisateur = load_user(form.email.data)
            login_user(utilisateur)
            return redirect(req.args.get("next") or url_for('index.index'))
    return render_template('/signin.html', form = form)




@signing_b.route('/signup/', methods=['GET','POST'])
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
            return redirect(url_for('index.index'))
    return render_template('signup.html', form = form)
