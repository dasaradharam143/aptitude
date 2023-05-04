a=int(input('enter 1st value = '))
b=int(input('enter increment percent of 3rd number'))
c=((b+100)/100)*a
d=int(input('enter increment percent of 2nd number'))
e=((d+100)/100)*c
f=int(input('enter 4th value'))
g=int(input('enter decrement percent of 4th number to 5th'))
h=f*100/(100-g)
list=[]
list.append(a)
list.append(c)
list.append(e)
list.append(f)
list.append(h)
print(list)
asc = sorted(list)
print(asc)
dsc = asc[::-1]

min_average = sum(asc)-asc[-1]/4
max_average = sum(dsc)-dsc[-1]/4
print(min_average)
print(max_average)
print('average difference= '+str(max_average - min_average))

# output:
# enter 1st value = 200
# enter increment percent of 3rd number25
# enter increment percent of 2nd number20
# enter 4th value350
# enter decrement percent of 4th number to 5th30
# [200, 250.0, 300.0, 350, 500.0]
# [200, 250.0, 300.0, 350, 500.0]
# average difference= 75.0