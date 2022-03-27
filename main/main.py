from flask import render_template, Blueprint, request

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def page():
    return render_template('index.html')
