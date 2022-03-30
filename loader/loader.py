from flask import render_template, Blueprint, request
from functions import json_dump
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO)

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', static_folder='static')
post_path = "posts.json"


@loader_blueprint.route('/post')
def page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=["Post"])
def page_post():
    allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    # Получаем объект картинки из формы
    picture = request.files.get("picture")
    # Получаем имя файла у загруженного фала
    filename = picture.filename
    # Получаем расширение файла
    extension = filename.split(".")[-1]
    if extension in allowed_extensions:
        # Сохраняем картинку под родным именем в папку uploads
        picture.save(f"./uploads/images/{filename}")
        content = request.form.get("content")
        picture_path = f"/post/{filename}"
        json_dump(picture_path, content)
        return render_template('post_uploaded.html', text=content, img=f'/post/{filename}')
    else:
        logging.info(f'Неверный тип файла: {extension}')
        return f"<h1> Тип файлов {extension} не поддерживается или файл не выбран </h1>"
