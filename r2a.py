R2A_MAP = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def getArabian(roman_character):
    try:
        arabian = R2A_MAP[roman_character];
        return arabian;
    except:
        return None;

def r2a(roman_number):
    parsed = 0;
    previous_arabian = None;
    for character in roman_number:
        arabian_character = getArabian(character);
        if (arabian_character == None):
            return None;
        if (previous_arabian != None and previous_arabian < arabian_character):
            parsed = parsed - 2 * previous_arabian;
        parsed = parsed + arabian_character;
        previous_arabian = arabian_character;
    return parsed;