# Notes Flask

Microframework de développement d'applicaitons web.

Basé sur le moteur de template Jinja2 et utilisant le WSGI (Web Server Gateway Interface) Werkzeug.

##### Installation

    $ sudo pip install Flask (installation globale)

L'installation peut également se faire dans un environnement virtuel (conseillé).

    $ sudo pip install virtualenv
    $ virtualenv venv // pour créer l'environnement virtuel
    $ . venv/bin/activate // activation de l'environnement

    $ deactivate // pour desactiver l'environnement


#### Première application Flask

````
from flask import Flask # On impore la classe Flask
app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello'
````
La fonction hello est exécuté quand un requête atteint le chemin spécifié dans le décorateur *route* passé à la classe qui contient l'application (*app*).

##### Ajout de variables

Les variables à l'intérieur des chemins sont spécifiées entre chevrons (*<variable>*). Peut être converti en faisant précédé la variable du type de conversion

    @app.route('/users/<int:user_id>')
