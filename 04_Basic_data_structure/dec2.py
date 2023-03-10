#dec
def decorator(func):
    def wrapper(*args):
        print('start decorator...')
        func(*args)
        print('end decorator...')

    return wrapper

def say(name, name2):
    print(name, 'say hello!!')
    print(name2)

say = decorator(say)
say('f', 'a')
