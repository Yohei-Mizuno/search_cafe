"""
TODO
    serch_cafeでぐるなびAPIから情報を受け取る｡
"""
import os

from cafe_module.address.input_user_address import input_user_address
from cafe_module.search.search_cafe import search_cafe


def main():
    URL = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
    KEY_ID = os.environ["key_id"]
    FREEWORD = 'cafe'
    hit_per_page = 10
    address = input_user_address()
    cafes = search_cafe(URL, KEY_ID, FREEWORD, hit_per_page, address)

    for cafe in cafes:
        print(cafe.get_cafe_info())


if __name__ == '__main__':
    main()
