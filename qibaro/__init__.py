from flask import Flask
from .view.admin import admin
from .view.feed import feed
from .view.inscription import inscription
from .view.profile import profile
from .view.usage import usage

# Enregistrement des Blueprint
app.register_blueprint(admin)
app.register_blueprint(feed)
app.register_blueprint(inscription)
app.register_blueprint(profile)
app.register_blueprint(usage)
