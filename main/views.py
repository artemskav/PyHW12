from flask import Blueprint, render_template, request

from exceptions import DataFileBrokenException
from functions import *
import logging

logging.basicConfig(filename="./basic.log", level=logging.INFO)


main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")

@main_blueprint.route("/")
def main_page():
    """ загрузка начальной страницы """
    return render_template("index.html")

@main_blueprint.route("/search/")
def search_page():
    """ Поиск по постах по запросу """
    s = request.values.get("s", None)
    logging.info(f"Created search by query: '{s}'")
    if s is None or s == '':
        posts = load_posts()
    else:
        posts = search_posts(s)
    return render_template("post_list.html", s=s, posts=posts)

@main_blueprint.errorhandler(DataFileBrokenException)
def error_load_file_crash(e):
    return "Файл постов поврежден"
