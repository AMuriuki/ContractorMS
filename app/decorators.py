from functools import wraps
from flask_login import current_user
from flask import flash, url_for, redirect

def admin_required(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        print (current_user.role)
        if current_user.role == "superuser":
            return function(*args, **kwargs)
        else:
            flash("You need superuser access to view this page")
            return redirect(url_for('auth.login'))

    return wrap