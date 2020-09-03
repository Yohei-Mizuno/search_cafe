import requests

from Cafe import Cafe


def search_cafe(URL, KEY_ID, FREEWORD, hit_per_page, address):
    response = requests.get(URL, params=dict(keyid=KEY_ID, freeword=FREEWORD, address=address,
                                             hit_per_page=hit_per_page))
    cafes = response.json()['rest']
    for cafe in cafes:
        yield Cafe(name=cafe['name'])
