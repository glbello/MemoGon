from definicion_item import Item
import json


def jsonToDict(path):
    with open(path, encoding="utf-8") as json_file:
        json_str = json_file.read()
        json_data = json.loads(json_str)

    return json_data


def dictToJson(path, data):
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=3)


if __name__ == '__main__':
    item_a = Item("raiz de 2", str(1.414))
    item_b = Item("raiz de 3", str(1.732))
    itemes = [1, 2,3]
    PATH_DATA = 'DATA.json'
    # data = jsonToDict(PATH_DATA)
    dictToJson(PATH_DATA, itemes)
