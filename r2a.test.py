testSuite = [
    {
        'description': 'Should return 1, when I given',
        'input': 'I',
        'expected': 1,
        'locked': False
    },
    {
        'description': 'Should return none, when not IVXCMLD given',
        'input': 'IVB',
        'expected': None,
        'locked': False
    },
    {
        'description': 'Should return 3, when III given',
        'input': 'III',
        'expected': 3,
        'locked': False
    },
    {
        'description': 'Should return 5, when V given',
        'input': 'V',
        'expected': 5,
        'locked': False
    },
    {
        'description': 'Should return 4, when IV given',
        'input': 'IV',
        'expected': 4,
        'locked': False
    },
    {
        'description': 'Should return 10, when X given',
        'input': 'X',
        'expected': 10,
        'locked': False
    },
    {
        'description': 'Should return 9, when IX given',
        'input': 'IX',
        'expected': 9,
        'locked': False
    },
    {
        'description': 'Should return 15, when XV given',
        'input': 'XV',
        'expected': 15,
        'locked': False
    },
        {
        'description': 'Should return 14, when XIV given',
        'input': 'XIV',
        'expected': 14,
        'locked': False
    },
    {
        'description': 'Should return 31, when XXXI given',
        'input': 'XXXI',
        'expected': 31,
        'locked': False
    },
    {
        'description': 'Should return 40, when XL given',
        'input': 'XL',
        'expected': 40,
        'locked': False
    },
    {
        'description': 'Should return 50, when L given',
        'input': 'L',
        'expected': 50,
        'locked': False
    },
    {
        'description': 'Should return 49, when LIX given',
        'input': 'XLIX',
        'expected': 49,
        'locked': False
    },
    {
        'description': 'Should return 101, when CI given',
        'input': 'CI',
        'expected': 101,
        'locked': False
    },
    {
        'description': 'Should return 101, when CD given',
        'input': 'CD',
        'expected': 400,
        'locked': False
    },
    {
        'description': 'Should return 500, when C given',
        'input': 'D',
        'expected': 500,
        'locked': False
    },
    {
        'description': 'Should return 900, when CM given',
        'input': 'CM',
        'expected': 900,
        'locked': False
    },
    {
        'description': 'Should return 950, when CML given',
        'input': 'CML',
        'expected': 950,
        'locked': False
    },
    {
        'description': 'Should return 999, when CMXCIX given',
        'input': 'CMXCIX',
        'expected': 999,
        'locked': False
    },
]

from r2a import r2a;
from testing import hope;
from testing import test;

for test_item in testSuite:
    description = test_item['description'];
    args = test_item['input'];
    expected = test_item['expected'];
    def testFunction():
        result = r2a(args);
        outcome = hope(result)['toBe'](expected);
        return outcome;
    if (test_item['locked'] != True):
        test(description, testFunction);
