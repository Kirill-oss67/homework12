import json

post_path = "posts.json"


def json_load(path):
    with open(path, "r", encoding='UTF-8') as file:
        data_ = json.load(file)
        return data_


data = json_load(post_path)


def search_by_json(json_data, string_):
    for i in json_data:
        if string_ in i['content']:
            return i

