# coding=utf-8
from datetime import datetime

# Flask extensions import
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, InputRequired, Regexp, Length
from flask_wtf.csrf import CSRFProtect

from flask_mongoalchemy import MongoAlchemy

from flask_bcrypt import Bcrypt

from flask_openid import OpenID

from flask_login import LoginManager, UserMixin

from flask_oauth import OAuth

db = MongoAlchemy()
bcrypt = Bcrypt() # Extension for passwords encrypting purpose
oid = OpenID()
login_manager = LoginManager()
login_manager.login_view = 'signing.signin'
login_manager.login_message = 'Veuilez-vous connecter pour continuer'
oauth = OAuth()
csrf = CSRFProtect()

# Forms definition
class LoginForm(FlaskForm):
    email = StringField(u'E-mail', [
                                InputRequired(),
                                Email()
                                    ])
    passwd = PasswordField(u'Mot de passe', [InputRequired()])

class RegistrationForm(FlaskForm):
    prenom = StringField(u'Prénom', [
                                        InputRequired("Veuillez entrer votre prénom")
                                    ])
    nom = StringField(u'Nom', [
                                    InputRequired("Veuillez entrer votre nom")
                                ])
    email = StringField(u'E-mail', [
                                        InputRequired(),
                                        Email("Une adresse e-mail est requise!")
                                    ])
    passwd = PasswordField(u'Créer un mot de passe', [
                                                InputRequired(),
                                                Length(min = 6, max = 10, message="Le mot de passe doit être compris entre 6 et 10 caractères")
                                            ])

# Collections definition
# Definition of the user Collection
class Utilisateur(db.Document):
    """Collection defining the users of the app"""

    prenom = db.StringField()
    nom = db.StringField()
    email = db.StringField()
    motdepasse = db.StringField()
    bio = db.StringField(required=False)
    profession = db.StringField(required=False)
    volontaire = db.BoolField(required=False, default=False)

    def is_authenticated():
        return True

    def is_active():
        return True

    def is_anonymous():
        return False

    def get_id():
        return self.email


# Publications document definition
class Publication(db.Document):
    """Publications collection definition"""

    auteur = db.StringField()
    titre = db.StringField()
    contenu = db.StringField()
    creation = db.CreatedField()
    commentaires = db.ListField(db.ObjectIdField(required=False))
    points = db.IntField(required=False, default=0)

# Comments Document definition
class Commentaire(db.Document):
    """Comments collection definition"""

    auteur = db.ObjectIdField()
    contenu = db.CreatedField()
    creation = db.CreatedField()
