import math


def denary_to_binary(number: int):
    binary = ''
    max_bit = math.log2(number)
    max_bit = int(str(max_bit).split('.')[0])

    while number != 0 or max_bit >= 0:
        if number - (2 ** max_bit) >= 0:
            number -= (2 ** max_bit)
            binary += '1'
        else:
            binary += '0'
        max_bit -= 1

        if max_bit < 0:
            break

    return binary


def binary_to_denary(binary: str):
    denary = 0
    binary = binary[::-1]
    for power, digit in enumerate(binary):
        if digit == '1':
            denary += 2 ** power

    return denary


def denary_to_hex(number: int):
    hex = ''
    hex_letters = '123456789ABCDEF'
    max_hex = math.log(number, 16)
    max_hex = int(str(max_hex).split('.')[0])

    while max_hex > -1:
        digit = number // 16 ** max_hex
        hex += hex_letters[digit - 1]
        number -= digit * 16 ** max_hex
        max_hex -= 1
        if number == 0:
            hex += '0' * (max_hex + 1)
            break

    return hex


def hex_to_denary(hex: str):
    hex_letters = '123456789ABCDEF'
    denary = 0
    hex = hex[::-1]
    for power, digit in enumerate(hex):
        denary += (int(hex_letters.find(digit)) + 1) * 16 ** int(power)

    return denary


if __name__ == '__main__':
    print(denary_to_binary(8))
    print(binary_to_denary('1000'))
    print(denary_to_hex(255))
    print(hex_to_denary('5F'))
