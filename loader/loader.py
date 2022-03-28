from flask import render_template, Blueprint, request
from functions import json_dump

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', static_folder='static')
post_path = "posts.json"


@loader_blueprint.route('/post')
def page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=["Post"])
def page_post():
    try:
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
            picture_path = f"/uploads/images/{filename}"
            json_dump(picture_path, content)
            return render_template('post_uploaded.html', text=content, img=f'/post{filename}')
        else:
            return f"<h1> Тип файлов {extension} не поддерживается </h1>"
    except:
        return f"<h1> Ошибка при загрузке файла </h1>"
