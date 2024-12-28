def hope(result):
    def toBe(expected):
        isAsHoped = result == expected
        if (isAsHoped):
            outcome = {
                'outcome': 'Pass',
            }
            return outcome
        else:
            outcome = {
                'expected': expected,
                'actual': result,
                'outcome': 'Fail'
            }
            return outcome;      
            
    return {'toBe': toBe};

def test(description, testFunction):
    result = testFunction();
    if (result['outcome'] == 'Pass'):
        message = 'Pass: %s' % description;
        print(message);
    else:
        message = 'Fail: %s' % description;
        explanation = 'Expected: %s Received: %s' % (result['expected'], result['actual']);
        print(message);
        print(explanation);
