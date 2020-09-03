def input_user_address():
    disable_list = ['<','>']
    add_1 = input('都道府県を入力>>>')
    address_1 = add_1.replace('<', '')

    # abcdefghijklmnopqrstuvwxyz!"#$%&()-=^~¥|@`[]{}:*;+<>,./?_
    add_2 = input('市区町村を入力>>>')
    address_2 = add_2.replace('<', ' ')
    return address_1 + address_2

def main():
    a = input_user_address()
    print(a)




if __name__ == '__main__':
    main()
