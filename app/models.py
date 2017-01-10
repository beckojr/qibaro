from datetime import datetime

# Flask extensions import
from flask_mongoalchemy import MongoAlchemy
from flask_bcrypt import Bcrypt

db = MongoAlchemy()
bcrypt = Bcrypt() # Extension for passwords encrypting purpose

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
