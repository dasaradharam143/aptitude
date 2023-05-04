

def fun1():                                          # page no 267 Qno 35
    a = int(input('enter ratio of man age = '))
    b = int(input('enter ratio son age = '))
    c = int(input('product of their ages = '))
    x = (c / (a * b)) ** 0.5
    print('x = ' + str(x))
    print(f'man age = {a}x = '+str(a * x)+' years')
    print(f'son age = {b}x = ' + str(b * x)+' years')
    d = int(input('enter hence years = '))
    p = a * x + d
    q = b * x + d
    print(f'ratio of their ages after {d} years = {p}/{q} = '+str(p / q))


def fun2():                                         # page no 266 Qno 18
    a = int(input('enter ratio of a age = '))
    b = int(input('enter ratio b age = '))
    h = int(input('enter hence years = '))
    c = int(input('enter ratio of a age after hence years = '))
    d = int(input('enter ratio of b age after hence years = '))
    p = (a*h*c-a*h*d)/(a*d - b*c)
    q = (b*h*c - b*h*d)/(a*d - b*c)
    print(f'difference of their ages = {p} - {q} = '+str(abs(q-p))+' years')


def fun3():                                             # page no 266 Qno 21
    a = int(input('sum of their ages a,b = '))
    b = int(input('enter ratio of mother = '))
    c = int(input('enter ratio of daughter = '))
    d = int(input('enter hence years = '))
    p = (a+c*d-b*d) / (c+b)
    q = (a*b - c*d + b*d) / (c+b)
    print(f'daughter age = {p} years')
    print(f'mother age = {q} years')


A = input('enter option 1 2 3 = ')
if A == '1':
    fun1()
elif A == '2':
    fun2()
elif A == '3':
    fun3()
else:
    print('enter valid input')