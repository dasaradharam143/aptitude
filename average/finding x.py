a = int(input('total count of numbers = '))
b = float(input('each number increased/decreased by = '))
average = float(input('average of numbers= '))
total = 0
for i in range(a):
    total += b * i
x = (a * average - total) / a
print('the numbers are ')
for i in range(a):
    print(str(x + (b * i)), end=' ')
