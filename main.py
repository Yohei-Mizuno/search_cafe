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



def input_user_address():
    disable_list = ['<','>']
    add_1 = input('都道府県を入力>>>')
    address_1 = add_1.replace('<', '')

    # abcdefghijklmnopqrstuvwxyz!"#$%&()-=^~¥|@`[]{}:*;+<>,./?_
    add_2 = input('市区町村を入力>>>')
    address_2 = add_2.replace('<', ' ')
    return address_1 + address_2




def search_cafe(address):
    response = requests.get(URL, params=dict(keyid=KEY_ID, freeword=FREEWORD, address=address,
                                             hit_per_page=hit_per_page))
    cafes = response.json()['rest']
    for cafe in cafes:
        yield Cafe(name=cafe['name'])


def main():
    address = input_user_address()
    cafes = search_cafe(address)

    for cafe in cafes:
        print(cafe.get_cafe_info())


if __name__ == '__main__':
    main()
