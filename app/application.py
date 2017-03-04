from flask import Flask

def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    from models import db, bcrypt, oid, login_manager, csrf

    db.init_app(app) # DB initialisation
    bcrypt.init_app(app) # Bcrypt hashing initialisation
    oid.init_app(app) # OpenID initialisation
    login_manager.init_app(app) # flask_login initialisation
    csrf.init_app(app) # CSRF Protection initialisation for all the app
    # oauth.init_app(app)

    # from app.views.about import about
    # from app.views.admin import admin
    from app.views.feed import feed
    # from app.profile.views import profile_b
    from app.views.signing import signing
    from app.views.post import post
    #from app.publications.views import publication_b

    # Registration of the blueprints
    # app.register_blueprint(about_b, url_prefixe="/about/")
    # app.register_blueprint(admin_b, url_prefixe="/admin/")
    app.register_blueprint(feed) # On arrive directement sur le feed qd on lance l'appli
    # app.register_blueprint(profile_b, url_prefixe="/profile/")
    app.register_blueprint(signing)
    app.register_blueprint(post)
    # app.register_blueprint(publication_b, url_prefixe="/publication/")
    # app.register_blueprint(layout_b)

    return app
