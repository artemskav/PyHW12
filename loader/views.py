from flask import Blueprint, render_template, request
from functions import *
import logging

logging.basicConfig(filename="./basic.log", level=logging.INFO)


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")

@loader_blueprint.route("/post", methods=['GET'])
def loader_page():
    return render_template("post_form.html")

@loader_blueprint.route("/post", methods=['POST'])
def page_upload():
    """ Эта вьюшка обрабатывает форму, вытаскивает из запроса файл и показывает его имя"""

    # Получаем объект картинки и текст из формы
    picture = request.files.get("picture", None)
    content = request.form.get("content", '')

    filename = picture.filename      # Получаем имя файла у загруженного файла

    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    extension = filename.split(".")[-1]     # Получаем расширение файла
    if extension in ALLOWED_EXTENSIONS:     # Если расширение файла в белом списке
        # Сохраняем картинку под родным именем в папку uploads
        picture.save(f"./uploads/{filename}")
    else:
        logging.info("Loading file - no picture")
        return f"Тип файлов {extension} не поддерживается"
    pict = f"/uploads/{filename}"
    save_json(pict, content)    # Запись JSON-файла
    return render_template("post_uploaded.html", picture=pict, content=content)
