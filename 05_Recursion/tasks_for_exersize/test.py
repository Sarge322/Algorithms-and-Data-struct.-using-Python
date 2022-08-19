j = 238
x = j % 10
print(x)
z = (j - x)/10
print(z)
x = z % 10
print('x',x)
z = (z - x)/ 10
print('z',z)
x = x % 10

print(x)
