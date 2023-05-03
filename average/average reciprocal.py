numbers = list(map(float, input('enter the numbers = ').split()))
b = []
for i in numbers:
    b.append(round(1 / i, 5))
print('reciprocals of numbers = ' + str(b))
total = round(sum(b), 5)
print('sum of numbers = ' + str(total))
avg = sum(b) / len(b)
print('average of numbers = ' + str(total) + '/' + str(len(b)) + ' = ' + str(round(avg, 5)))
