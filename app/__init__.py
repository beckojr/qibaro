from flask import Flask
from app.about.views import about_b
from app.admin.views import admin_b
from app.index.views import index_b
from app.profile.views import profile_b
from app.signing.views import signing_b

app = Flask('__name__', static_folder=None)
app.register_blueprint(about_b, url_prefixe="/about/")
app.register_blueprint(admin_b, url_prefixe="/admin/")
app.register_blueprint(index_b) # On arrive directement sur le feed qd on lance l'appli
app.register_blueprint(profile_b, url_prefixe="/profile/")
app.register_blueprint(signing_b, url_prefixe="/signing/")
