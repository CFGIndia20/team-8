from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

# there is another method called errorhandler but that will only be valid for this blue print but we want this error handler to work across the entire application so use app_errorhandler
@errors.app_errorhandler(404)
def error_404(error):
	# second value while returning is the status code
	# in flask by default it is 200 but here we have to mention 404
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500