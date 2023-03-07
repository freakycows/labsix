def hex_char_decode(digit):
    value = 0
# below gives the number inputted a value
    if digit == '0':
        value = 0
    if digit == '1':
        value = 1
    if digit == '2':
        value = 2
    if digit == '3':
        value = 3
    if digit == '4':
        value = 4
    if digit == '5':
        value = 5
    if digit == '6':
        value = 6
    if digit == '7':
        value = 7
    if digit == '8':
        value = 8
    if digit == '9':
        value = 9
# below gives number value to a letter in hexadecimal system
    if digit == 'A' or digit == "a":
        value = 10
    if digit == 'B' or digit == 'b':
        value = 11
    if digit == 'C' or digit == 'c':
        value = 12
    if digit == 'D' or digit == 'd':
        value = 13
    if digit == 'E' or digit == 'e':
        value = 14
    if digit == 'F' or digit == 'f':
        value = 15

    return value


def hex_converter(digit):  # this is for converting binary to hex in option 3
    value = int(digit)
    if value < 10:  # if the number is less than 10 it takes the number at face value
        return digit
    if value == 10:
        return 'A'
    if value == 11:
        return 'B'
    if value == 12:
        return 'C'
    if value == 13:
        return 'D'
    if value == 14:
        return 'E'
    if value == 15:
        return 'F'


def hex_string_decode(hex):  # this def decodes hexadecimal to decimal
    if hex[0] == '0' and hex[1] == 'x':  # this ignores if the number is inputted with 0x at the beginning
        hex = hex[2:]
    total = 0
    bit_index = len(hex)
    for digit in range(bit_index):
        total += hex_char_decode(hex[digit]) * (16 ** (bit_index - digit - 1))
    return int(total)


def binary_string_decode(binary):  # this def decodes binary to decimal
    if binary[0] == '0' and binary[1] == 'b':  # this ignores if the number is inputted with 0b at the beginning
        binary = binary[2:]
    bit_index = len(binary)
    total = 0
    for digit in range(bit_index):
        if binary[digit] == '1':
            total += (2 ** (bit_index - digit - 1))
    return total


def binary_to_hex(binary):  # this def converts binary to hexadecimal
    res = ""
    value = binary_string_decode(str(binary))
    while value > 0:
        res = str(hex_converter(str(value % 16))) + res
        value //= 16

    return res


def main():  # idea from Andrew's video
    while True:
        print('''Decoding Menu 
    ------------- 
    1. Decode hexadecimal 
    2. Decode binary 
    3. Convert binary to hexadecimal 
    4. Quit''')
# prints out the number calculate based on which option is chosen
        option = int(input('\nPlease enter an option: '))
        if option == 1:
            hex = input("Please enter the numeric string to convert: ")
            print('Result:', hex_string_decode(hex), '\n')
        if option == 2:
            binary = input("Please enter the numeric string to convert: ")
            print('Result:', binary_string_decode(binary), '\n')
        if option == 3:
            binary = input("Please enter the numeric string to convert: ")
            print('Result:', binary_to_hex(binary), '\n')
        if option == 4:
            break
    print('Goodbye!')


if __name__ == '__main__':
    main()  # print's the option chosen from def main()
