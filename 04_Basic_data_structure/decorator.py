def func():
    print("This is decorated func")

def dec(f):
    print('111')
    f
    print('222')

dec(func())