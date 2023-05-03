

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

def fun2():
    pass

a=input('enter option 1 2 3 = ')
if a=='1':
    fun1()
elif a=='2':
    fun2()