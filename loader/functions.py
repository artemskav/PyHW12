import json

from pprint import pprint as pp

def load_posts():
    with open("../posts.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def search_posts(query):
    post_by_query = []
    posts = load_posts()
    for post in posts:
        if query in post["content"]:
            post_by_query.append(post)
    return post_by_query
