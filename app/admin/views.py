from flask import url_for, redirect
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from app import current_app, _admin, db
from app.models import User, Role
# from app.decorators import admin_required


class UserModelView(ModelView):
    def is_accessible(self):
        roles = []
        user_roles = current_user.roles
        for user_role in user_roles:
            roles.append(user_role.name)            
        return (current_user.is_active and current_user.is_authenticated and "superuser" in roles)

    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('auth.login'))


class _AdminIndexView(AdminIndexView):
    def is_accessible(self):
        roles = []
        user_roles = current_user.roles
        for user_role in user_roles:
            roles.append(user_role.name)            
        return (current_user.is_active and current_user.is_authenticated and "superuser" in roles)

    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('auth.login'))