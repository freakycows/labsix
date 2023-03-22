def encode(num):
    password = ''
    for i in num:
        added_num = str((int(i) + 3) % 10)  # % 10 returns the second digit if i > 10
        password += added_num
    return password


def decode(num):
    pass


image_data = None


def menu():
    option = '1'
    while option != '0':  # taken from Andrew's template
        print('''Menu  
------------- 
1. Encode  
2. Decode  
3. Quit ''')
        option = input('\nPlease enter an option: ')
        if option == '1':
            encode_num = input('Please enter your password to encode: ')
            image_data = encode(encode_num)  # encodes and stores the number entered to use in option 2 and
            print("Your password has been encoded and stored!")
        if option == '2':
            encode_method = image_data
            decode_method = decode(image_data)  # decodes the number encoded
            print("The encoded password is", encode_method, "and the original password is", decode_method, end=".\n")
        if option == '3':
            break


if __name__ == "__main__":
    menu()
