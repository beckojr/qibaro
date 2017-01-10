from flask import Blueprint, render_template, abort, redirect, request, current_app, url_for
from jinja2 import TemplateNotFound
from app.models import Utilisateur

signing_b = Blueprint('signing', __name__,
                                template_folder='templates',
                                static_folder='static_s')

@signing_b.route('/signin/', methods=['GET', 'POST'])
def signin():
    return render_template('/signin.html')
    # if request.method == 'GET':
    #     return render_template('/signin.html')
    # elif request.method == 'POST':
    #




@signing_b.route('/signup/', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        # signing up
        nw_user = Utilisateur(
                    prenom = request.form['i-prenom'],
                    nom = request.form['i-nom'],
                    email = request.form['i-email'],
                    motdepasse = request.form['i-passwd'])
        nw_user.save()
        return redirect(url_for('.signin'))
    elif request.method == 'GET':
        return render_template('signup.html')
