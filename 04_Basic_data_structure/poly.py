def is_polyndrome(str):
    return str == "".join(reversed(str))

def test():
    tests=[
        ('abba', True),
        ('ab rba', False),
        (' roor ', True),
        ('bacab', True),
        ('abbacc', False),

    ]
    for i in tests:
        line = i[0]
        try:
            res = is_polyndrome(line)
            assert i[1] == res
        except Exception as e:
            print(e)
            return False
    return True

if __name__ == '__main__':
    if test():
        print('Tested, all oK!')
    else:
        print('Failed!')