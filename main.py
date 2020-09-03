"""
TODO
    serch_cafeでぐるなびAPIから情報を受け取る｡
"""
import requests

URL = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
KEY_ID = '41c9d06d00a75002e081b8097f9ae199'
FREEWORD = 'cafe'
hit_per_page = 10


class Cafe(object):
    def __init__(self, name):
        self.name = name

    def get_cafe_info(self):
        return f"Name:{self.name}"


def search_cafe(address):
    response = requests.get(URL, params=dict(keyid=KEY_ID, freeword=FREEWORD, address=address,
                                             hit_per_page=hit_per_page))
    cafes = response.json()['rest']
    for cafe in cafes:
        yield Cafe(name=cafe['name'])


def main():
    address = '埼玉県'
    cafes = search_cafe(address)

    for cafe in cafes:
        print(cafe.get_cafe_info())


if __name__ == '__main__':
    main()
