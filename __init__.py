# this file tells python that this is a package , also initialises and ties together everything we need for our app
# even if __init__.py file is empty python will get to know that are packages

# import os  #to be able to use environment variables
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
# importing config class that we created
from flaskblog.config import Config

# not moving these extensions inside class bcoz we want extensions to be created for all the instances 

# creating an instance of SQLAlchemy
db = SQLAlchemy()
bcrypt = Bcrypt()
# login manager handles all the sessions for us in the background
login_manager = LoginManager()
# 'login' is the func name of our route
login_manager.login_view = 'users.login'
# 'info' is bootstrap class 
login_manager.login_message_category = 'info'

# initialising the extension
mail = Mail()


# before creating blueprints was importing routes like this but now will import blueprint objects from each of those packages and will register them with the route
# cant import routes at the top of this file otherwise gets into circular inputs
# from flaskblog import routes

# allow us to create diff instances of our class for diff configurations
def create_app(config_class=Config):
    app = Flask(__name__)  #will import this in run.py
    app.config.from_object(Config)

    # for each of the extension running init_app method and pass the app as parameter
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app