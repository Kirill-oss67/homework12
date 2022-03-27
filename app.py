from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from main.main import main_blueprint
from functions import search_by_json, json_load
from loader.loader import loader_blueprint

post_path = "posts.json"
UPLOAD_FOLDER = "uploads/images"

data = json_load(post_path) # Получаем данные из json файла

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route('/search')
def search_page():
    s = request.args.get('s')
    searched_data = search_by_json(data, s)
    return render_template("post_list.html", search=s, dict_key1=searched_data["pic"],
                           dict_key2=searched_data["content"], )


#
# @app.route("/list")
# def page_tag():
#     pass
#
#
# @app.route("/post", methods=["GET", "POST"])
# def page_post_form():
#     pass
#
#
# @app.route("/post", methods=["POST"])
# def page_post_upload():
#     pass
#
#
# @app.route("/uploads/<path:path>")
# def static_dir(path):
#     return send_from_directory("uploads", path)


app.run(debug=True, port=5001)
