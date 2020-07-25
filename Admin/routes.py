from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email

# a flask blueprint is a way for you to organize your flask application into smaller and re-usable application. 
# Just like a normal flask application, a blueprint defines a collection of views, templates and static assets.
admin = Blueprint('admin', __name__)

# will not use global app variable to create routes like before instead will use app variables specific to this blueprint to register these with our application at a later time


# writing methods=['GET' , 'POST'] will allow us to get or post data from this URL 
# otherwise error comes - this method is not allowed for requested URL
# @app.route("/register", methods=['GET', 'POST'])
# using users.route instead of app.routes
@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    # to check whether form submitted correctly or not
    if form.validate_on_submit():
        # hashing the password for security purpose
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # creating a new user
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        # adding new user to the database
        db.session.add(user)
        db.session.commit()
        # flash is one t@userspop up message 
        # writing f in flash message bcoz it is a flash string--> syntax it is (f strings used in python 3.6 and above)
        # passing success as second argument just a bootstrap class(that we want flash message to have) bcoz flash accepts ALERT as 2nd argument  
        flash(f'Account created for {form.username.data}!', 'success')
        # redirecting user to home page after successful submission to avoid any confusion for the user
        # url_for (name of the function where have to redirect and not the route name)
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # args is a dictionary, but we don't want ot access it using name and square brackets bcoz that will raise an error if key doesn't exist
            # now it will simply return none if the key value doesn't exist
            next_page = request.args.get('next')
            # ternary condition in python
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    # creating an instance of updateAccountForm
    form = UpdateAccountForm()
    if form.validate_on_submit():
        # checking if user wants to update profile pic or not bcoz it's not a required field
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        # SQLAlchemy makes it easy to simply update the values and commit them to the database
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        # redirecting to the account page again 
        return redirect(url_for('users.account'))
    # if there's a GET request then populate the fields with current user's data
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    # image_file in url_for is name of the field in table 
    # go to static directory, then profile_pics then image_file
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    # passing image file as 3rd parameter to accounts template bcoz using this image there
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


# whenever a particular username is clicked all his posts are displayed
# dynamic parametr- string:username
@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    # get the first user with this username or if it does not exist then return 404 
    user = User.query.filter_by(username=username).first_or_404()
    # putting \ to be able to break this line into multiple lines
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


# requesting to reset the password
@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        # after form is submitted grabbing the user with that email
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


# actually resetting the password
@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    # defined this func in models.py already
    user = User.verify_reset_token(token)
    # if doesn't gets back a user then that means token is invalid or expired
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)