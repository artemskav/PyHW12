import json
import logging

from exceptions import DataFileBrokenException

logging.basicConfig(filename="basic.log", level=logging.INFO)

def load_posts():
    """ загрузка и преобразование JSON-файла"""
    try:
        with open("posts.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.info("Error load of JSON-file")
        raise DataFileBrokenException("Файл с данными поврежден")

def search_posts(query):
    """ Ф-я поиска по ключевому слову"""
    post_by_query = []
    posts = load_posts()
    for post in posts:
        if query in post["content"].lower():
            post_by_query.append(post)
    return post_by_query


def save_json(pic, content):
    """ Ф-я дописывания нового поста к файлу JSON"""
    data = load_posts()
    data.append({"pic": pic, "content": content})
    with open("posts.json", "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
