from functools import wraps
from flask_login import current_user
from flask import flash, url_for, redirect

def admin_required(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        roles = []
        user_roles = current_user.roles
        for user_role in user_roles:
            roles.append(user_role.name)
            print(roles)
        if "superuser" in roles:
            return function(*args, **kwargs)
        else:
            flash("You need superuser access to view this page")
            return redirect(url_for('auth.login'))

    return wrap