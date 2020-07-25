# contains all functions that are specific to user package

# importing os model to grab the extension of the image file uploaded by the user
import os
# importing secrets model to generate hex value 
import secrets
# was installed with pip3 install Pillow
from PIL import Image
from flask import url_for, current_app
# we want to send email message also 
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    # randomising the name of the picture uploaded by user bcoz oetherwise then it may collide with some other users pic name
    random_hex = secrets.token_hex(8)
    # grabbing the same file extension as uploaded by the user 
    # splittext returns two values - name of the file without extension, extension itself
    # in our app we'll not be using filename ever so its a good practice to drop the names of unused variables
    # in python it's done using _
    _, f_ext = os.path.splitext(form_picture.filename)
    # craeting a new name for the image file by combining the hex name and the file extension
    picture_fn = random_hex + f_ext
    # getting the root path of our app all the way upto packages also 
    # getting the path by joining the root path and that where we want to store the image
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    # resizeing the image when user uploads it 
    # user might upload a very large pic but we have scaled it down to 125 px in main.css 
    # so scale down the size here also otherwise will occupy more space in database uselessly and will cause the website to run slow bcoz every time that large image has to be sent to the web browser
    output_size = (125, 125)
    # craeting a new image i
    i = Image.open(form_picture)
    # resizeing i
    i.thumbnail(output_size)
    # saving this new image i
    i.save(picture_path)

    return picture_fn


# using another flask extension, flask-mail
def send_reset_email(user):
    # this func already defined in User modal
    token = user.get_reset_token()
    # first parameter- subject line
    # second parameter- don't spoof a sender, if you will try to be someone you are not then will end up in spam folder so use something from your domain or email address
    msg = Message('Password Reset Request',
                  sender='noreply@gmail.com',
                  recipients=[user.email])
    # msg = Message('Password Reset Request',
    #               recipients=[user.email])
    # multi line string message
    # here only 1 {} for url bcoz its an f string
    # message lines indented same as base line wihtout any tab otherwise tab will also be displayed in message and we don't want that 
    # _external=true to get an absolute URL instead of relative URL bcoz relative URLs are fine within our application and thats what it normally returns
    # but the link in the email needs to have full domain 
    # Jinja2 templates can be used to peice the message together if it's too complicated
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)