def input_user_address():
    add_1 = input('都道府県を入力>>>')
    address_1 = add_1.replace('<', '')
    add_2 = input('市区町村を入力>>>')
    address_2 = add_2.replace('<', ' ')
    return address_1 + address_2
