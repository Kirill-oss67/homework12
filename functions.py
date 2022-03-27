import json
from json import JSONDecodeError

post_path = "posts.json"


def json_load(path=post_path):
    try:
        with open(path, "r", encoding='UTF-8') as file:
            data_ = json.load(file)
            return data_
    except FileNotFoundError:
        print("Файл не найден")
    except JSONDecodeError:
        # Будет выполнено, если файл найден, но не превращается из JSON
        print("Файл не удается преобразовать")


def json_dump(pic, cont):
    data = json_load()
    for_append = {"pic": pic, "content": cont}
    data.append(for_append)
    with open(post_path, 'w', encoding='UTF-8') as f:
        json.dump(data, f, indent=4,ensure_ascii=False)


# data = json_load(post_path)


def search_by_json(json_data, string_):
    for i in json_data:
        if string_ in i['content']:
            return i
