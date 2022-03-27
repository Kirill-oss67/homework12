from flask import render_template, Blueprint, request

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', static_folder='static')


@loader_blueprint.route('/post')
def page():
    return render_template('post_form.html')


