import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin import Admin, helpers as admin_helpers
from flask_mail import Mail
from flask_babel import Babel, lazy_gettext as _l
from flask_admin.contrib.sqla import ModelView



db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
babel = Babel()
_admin = Admin()
mail = Mail()


def create_app(Config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    babel.init_app(app)
    
    from app.models import User, Role
    from app.admin.views import UserModelView, _AdminIndexView

    _admin.init_app(app, index_view=_AdminIndexView())
    _admin.add_view(UserModelView(User, db.session))
    _admin.add_view(UserModelView(Role, db.session))
    mail.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'],
                        app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject='ContractorMS Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/contractorMS.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('ContractorMS startup')

    return app

from app.models import User, Role

app = create_app()

@app.before_first_request
def build_sample_db():
    """
    Populate a small db with some example entries.
    """
    user = db.session.query(User).first()
    if user is None:
        import string
        import random

        db.drop_all()
        db.create_all()

        with current_app.app_context():
            user_role = Role(name='user', description='Normal user')
            super_user_role = Role(name='superuser', description='Super user')
            db.session.add(user_role)
            db.session.add(super_user_role)
            db.session.commit()

            super_user = User(
                first_name='Arnold',
                last_name='Muriuki',
                middle_name='Nderitu',
                username='amuriuki',
                email='arnoldnderitu@gmail.com',
                password_hash=generate_password_hash('admin'),
                roles=[user_role, super_user_role]
            )

            first_names = [
                'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie', 'Sophie', 'Mia',
                'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
                'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
            ]

            last_names = [
                'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
                'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
                'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
            ]

            for i in range(len(first_names)):
                tmp_email = first_names[i].lower() + "." + last_names[i].lower() + "@example.com"
                # tmp_pass = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(10))
                tmp_pass = first_names[i]
                user = User(
                    first_name = first_names[i],
                    last_name = last_names[i],
                    email = tmp_email,
                    password_hash = generate_password_hash(tmp_pass),
                    roles = [user_role, ]
                )
                db.session.add(user)            
            db.session.commit()
    return


# @babel.localeselector
# def get_locale():
#     return request.accept_languages.best_match(current_app.config['LANGUAGES'])
    

from app import models