#!/usr/bin/python3
def roman_to_int(roman_string):

    r = roman_string

    is_string = isinstance(roman_string, str)
    if is_string is False or roman_string is None:
        return 0

    rom_num = 0
    if "M" in roman_string:
        M = roman_string.count("M")
        M = M * 1000
        rom_num += M

    if "I" in roman_string:
        rom_I = roman_string.count("I")
        if r.find("I") < r.find("V") or r.find("I") < r.find("X"):
            rom_num -= 1
        else:
            rom_num += rom_I

    if "V" in roman_string:
        V = roman_string.count("V")
        V = V * 5
        rom_num += V

    if "X" in roman_string:
        X = roman_string.count("X")
        X = X * 10
        if r.find("X") < r.find("L") or r.find("X") < r.find("C"):
            rom_num -= 10
        else:
            rom_num += X

    if "L" in roman_string:
        L = roman_string.count("L")
        L = L * 50
        rom_num += L

    if "C" in roman_string:
        C = roman_string.count("C")
        C = C * 100
        if r.find("C") < r.find("D") or r.find("C") < r.find("M"):
            rom_num -= 100
        else:
            rom_num += C

    if "D" in roman_string:
        D = roman_string.count("D")
        D = D * 500
        rom_num += D

    return rom_num
