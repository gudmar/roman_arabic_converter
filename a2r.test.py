test_suite = [
    (1, 'I'),
    (2, 'II'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (9, 'IX'),
    (10, 'X'),
    (11, 'XI'),
    (14, 'XIV'),
    (15, 'XV'),
    (20, 'XX'),
    (21, 'XXI'),
    (24, 'XXIV'),
    (39, 'XXXIX'),
    (40, 'XL'),
    (44, 'XLIV'),
    (49, 'XLIX'),
    (50, 'L'),
    (60, 'LX'),
    (90, 'XC'),
    (100, 'C'),
    (101, 'CI'),
    (199, 'CXCIX'),
    (200, 'CC'),
    (400, 'CD'),
    (500, 'D'),
    (600, 'DC'),
    (900, 'CM'),
    (2000, 'MM')
]

def get_verboose_test_case(test_case):
    input, output = test_case;
    result = {
        'input': input,
        'output': output,
        'description': 'Should return %s when %s given' % (output, input),
    }
    return result

from a2r import a2r;

for test_item in test_suite:
    test_case = get_verboose_test_case(test_item)
    print(test_case['input'])
    result = a2r(test_case['input'])
    try:
        assert result == test_case['output']
    except:
        raise Exception('Input: %s, expected: %s, got: %s' % (test_case['input'], test_case['output'], result))
