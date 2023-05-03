total_count = int(input('total count of numbers = '))
value = float(input('each number increased/decreased by = '))
average = float(input('average of total numbers= '))
total = 0
for i in range(total_count):
    total += value * i
x = (total_count * average - total) / total_count
print('the numbers are: ')
for i in range(total_count):
    print(str(x + (value * i)), end=' ')
