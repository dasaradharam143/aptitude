a=int(input('enter no of members = '))
b=int(input('enter average of members = '))
c=int(input('enter highest members = '))
d=int(input('enter lowest of members = '))
e = int(input('difference between two numbers = '))
total = a*b
print('total = '+str(total))
formula = (total - c - d - e )/2
print('required number = '+str(formula))
numbers = []
numbers.append(formula)
numbers.append(formula+e)
numbers.append(c)
numbers.append(d)
print(numbers)
print('highest number = '+str(max(numbers)))

# output:
# enter no of members = 4
# enter average of members = 59
# enter highestf members = 83
# enter lowest of members = 29
# difference between two numbers = 28
# total = 236
# required number = 48.0
# [48.0, 76.0, 83, 29]
# highest number = 83
