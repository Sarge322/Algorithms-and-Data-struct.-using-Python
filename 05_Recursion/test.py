from turtle import *
color('red', 'yellow')
begin_fill()
ps = 4
x = 1
while True:
    pensize(ps)
    if x%10 == 0:
        ps = ps - 1
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
    x = x + 1
end_fill()
done()