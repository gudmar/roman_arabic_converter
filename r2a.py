R2A_MAP = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
R2A_DOUBLES = [
    'IV', 'IX', 'XL','XC', 'CD', 'CM'
]

def get_arabic_factor(roman_character):
    try:
        arabian = R2A_MAP[roman_character];
        return arabian;
    except:
        return None;

def check_if_double_latin_character_case(previous_roman, roman):
    double = '%s%s' % (previous_roman, roman);
    isLegalDouble = R2A_DOUBLES.count(double) > 0;
    return isLegalDouble;

def r2a(roman_number):
    parsed = 0;
    previous_arabian = None;
    previous_latin = None;
    for character in roman_number:
        arabic_factor = get_arabic_factor(character);
        if (arabic_factor == None):
            return None;
        is_double_latin_character_case = check_if_double_latin_character_case(previous_latin, character)
        if (is_double_latin_character_case == False and previous_arabian != None and previous_arabian < arabic_factor):
            return None
        if (is_double_latin_character_case):
            parsed = parsed - 2 * previous_arabian;
        parsed = parsed + arabic_factor;
        previous_arabian = arabic_factor;
        previous_latin = character;
    return parsed;