from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
# from __main__ import db
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# a class in SQLAlchemy represents a table in DB
# inheriting from db.Model so passing it as an argument
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # password 60 chars long bcoz we'll hash it then it will become long 
    password = db.Column(db.String(60), nullable=False)
    # posts attribute has an relationship with Post model, backref will add a new column to post model, 
    # lazy = true defines to load the data from the database
    # getting all the posts from post model that a particular user has created 
    # here 'Post' , capital P used here bcoz referring to a model and not a particular column
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800): #expires in 1800 sec i.e. 30 mins by default
        # s is an object of serializer 
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        # creating a token
        # {'user_id': self.id} - passing a payload
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod #basically telling python not to expect any self parametre in func call
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        # token could be invalid or could have been expired
        # so to handle exception putting in try/catch block
        try:
            # trying to get user_id from payload
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    # this func is used to control how our object will be printed
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


