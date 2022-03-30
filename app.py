from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from functions import search_by_json, json_load
from loader.loader import loader_blueprint
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO)

post_path = "posts.json"
IMAGES_FOLDER = "./uploads/images/"
data = json_load()  # Получаем данные из json файла

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route('/search')
def search_page():
    try:
        s = str(request.args.get('s')).lower()
        logging.info(f"Search's phrase is : {s}")
        searched_data = search_by_json(data, s)
        return render_template("post_list.html", search=s, searched_data=searched_data)
    except:
        return f"<h1> С таким именем ничего нет </h1>"


@app.route(f'/post/<path:path>')
def img_dir(path):
    return send_from_directory(IMAGES_FOLDER, path)


# @app.route(f'/uploads/images/<path:path>')
# def img_dir2(path):
#     return send_from_directory('uploads/images', path)


app.run(debug=True, port=5005)

# http://127.0.0.1:5005/post
