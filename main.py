"""
TODO
    serch_cafeでぐるなびAPIから情報を受け取る｡
"""
import os
import requests

from Cafe import Cafe

URL = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
KEY_ID = os.environ["key_id"]
FREEWORD = 'cafe'
hit_per_page = 10


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
