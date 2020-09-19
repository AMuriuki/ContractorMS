from flask import url_for, redirect
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from app import current_app, admin, db
from app.models import User, Role

class UserModelView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated)

    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('auth.login'))


admin.add_view(UserModelView(User, db.session))
admin.add_view(UserModelView(Role, db.session))