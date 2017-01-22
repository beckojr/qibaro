# coding=utf-8

from flask import Blueprint, render_template, abort, redirect, request, current_app, url_for, flash
from jinja2 import TemplateNotFound
from app.models import Utilisateur
from ..models import bcrypt, login_manager, LoginForm, RegistrationForm

signing_b = Blueprint('signing', __name__,
                                template_folder='templates',
                                static_folder='static_s')

# Tells to Flask how to load a user given his e-mail
@login_manager.user_loader
def load_user(user):
    return Utilisateur.query.get(user)

@signing_b.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        load_user(form.utilisateur)
        flash("Connexion réussie")
        return redirect(request.args.get("next") or url_for('index.index'))
    return render_template('/signin.html', form = form)




@signing_b.route('/signup/', methods=['GET','POST'])
def signup():
    form = RegistrationForm()

    if form.validate_on_submit():
        utilisateur = Utilisateur()

        # form.populate_obj(utilisateur)
        utilisateur.prenom = form.prenom.data
        utilisateur.nom = form.nom.data
        utilisateur.email = form.email.data
        utilisateur.motdepasse(form.passwd.data)
        utilisateur.save()

        load_user(utilisateur)
        return redirect(url_for('index.index'))
    return render_template('signup.html', form = form)
