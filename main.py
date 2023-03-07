def binary_to_hexadecimal(binary):
    decimal = 0
    hex_digits = "0123456789ABCDEF"
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * 2**power
        power -= 1
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal //= 16
    return hexadecimal


if __name__ == '__main__':
    option = int(input("enter:"))
    if option == 1:
        binary = input("enter")
        print(binary_to_hexadecimal(binary))
