from sys import argv

script, filename = argv
with open(filename, 'r+') as target:
    m = target.readlines()
    print(m)
    target.truncate(0)
    l1 = input("enter: ")
    l2 = input("enter: ")
    l3 = input("enter: ")
    target.write(l1)
    target.write('\n')
    target.write(l2)
    target.write('\n')
    target.write(l3)
