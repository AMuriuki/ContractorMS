# Building a secure admin interface with Flask-Admin and Flask-Security

**Goal: Implement authentication and authorization with Flask-Security**

The basic building block of authorization and authentication are users and user roles. Users represent the people with access to the application and user roles represent the various roles that these people will be assigned which will determine the parts of the application they have access to.

First step is to add the data models that represent users and user roles. 

```python
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean())
    password_hash = db.Column(db.String(128))
    roles = db.relationship(
        'Roles', secondary=user_roles_table, backref='user', lazy=True)
    
class Roles(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
```

I have a `user_roles_table` table which will be used as a helper table. This helper table is needed for the many-to-many relationship between users and user roles, i.e. one user can have many roles and one role can have many users.

```python
user_roles_table = db.Table('user_roles',
                            db.column('user_id', db.Integer(),
                                      db.ForeignKey('user.id')),
                            db.Column('roles_id', db.Integer(), db.ForeignKey('roles.id')))
```

