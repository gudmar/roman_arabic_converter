arabic_to_roman_map = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
]

def a2r(arabic_number):
    result = ''
    number = arabic_number
    for arabic, roman in arabic_to_roman_map:
        quantity = int(number / arabic)
        factor = quantity * arabic
        number -= factor
        result = '%s%s' % (result, quantity * roman)

    return result
    