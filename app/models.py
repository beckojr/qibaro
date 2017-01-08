from datetime import datetime
from flask.ext.mongokit import MongoKit, Document

# Import of the DB
from app import db

# Definition of the user Collection
class Utilisateur(Document):
    """Collection defining the users of the app"""

    __collection__ = 'utilisateur'
    structure {
        'prenom': str,
        'nom': str,
        'email': str,
        'motpasse': str,
        'bio': str,
        'profession': str,
    }

    required_fields = ['prenom', 'nom', 'email', 'motpasse']
    use_dot_notation = True

# Publications document definition
class Publication(Document):
    """Publications collection definition"""
    __collection__ = 'publication'
    structure {
        'auteur': str,
        'titre': str,
        'contenu': str,
        'creation': datetime,
        'commentaires': list,
        'points': int,
    }
    required_fields = ['titre', 'contenu', 'auteur']
    default_values = {'creation': datetime.utcnow}
    use_dot_notation = True

# Comments Document definition
class Commentaire(Document):
    """Comments collection definition"""
    __collection__ = 'commentaire'
    structure {
        'auteur': str,
        'contenu': str,
        'creation': datetime,
    }
    required_fields = ['auteur', 'contenu']
    default_values = {'creation': datetime.utcnow}
    use_dot_notation = True


# Registration of the definitions
db.register([Utilisateur, Publication, Commentaire])
