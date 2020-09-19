from flask import url_for, current_app
from app import security, admin, db, user_datastore
from flask_admin import helpers as admin_helpers
from flask_security.utils import encrypt_password
from app.models import User, Role

# define a context processor for merging flask-admin's template context
# into the flask-security views.
