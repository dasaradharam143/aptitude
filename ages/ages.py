

def fun1():                                          # page no 267 Qno 35
    a = int(input('enter ratio of man age = '))
    b = int(input('enter ratio son age = '))
    c = int(input('product of their ages = '))
    x = (c / (a * b)) ** 0.5
    print('x = ' + str(x))
    print('man age = '+str(a * x))
    print('son age = ' + str(b * x))
    d = int(input('enter hence years = '))
    p = a * x + d
    q = b * x + d
    print(f'ratio of their ages after {d} years = '+str(p / q))

def fun2():                                         # page no 266 Qno 18
    a = int(input('enter ratio of a age = '))
    b = int(input('enter ratio b age = '))
    h = int(input('enter hence years = '))
    c = int(input('enter ratio of a age after hence years = '))
    d = int(input('enter ratio of b age after hence years = '))
    p= (a*h*c-a*h*d)/(a*d - b*c)
    q= (b*h*c - b*h*d)/(a*d - b*c)
    print(p-q)


def fun3():


a=input('enter option 1 2 3 = ')
if a=='1':
    fun1()
elif a=='2':
    fun2()
else:
    fun3()