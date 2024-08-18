import json
import os

from src.product import Product
from src.category import Category


PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "products.json")

def read_json(path_to_file: str=PATH_TO_FILE) -> list:
    """ Читает JSON-файл """
    with open(path_to_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def create_object_from_json(data):
    """ Создает экземпляры класса из JSON-файла """
    categorys = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categorys.append(Category(**category))

    return categorys


if __name__ == '__main__':
    categorys_data = create_object_from_json(read_json())
    print(categorys_data[0].name)
    print(categorys_data[0].description)
    print(categorys_data[0].products)
