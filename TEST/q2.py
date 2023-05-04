numbers = list(map(float, input('enter the numbers = ').split()))
n = len(numbers)
total = sum(numbers)
average = total / n
print('sum of numbers = ' + str(total))
print('average of numbers = ' + str(total) + '/' + str(n) + ' = ' + str(round(average, 5)))

less_than_mean=[]
for i in numbers:
    if i<average:
        less_than_mean.append(i)
        # print(i)
print(less_than_mean)
print('people with less than mean salary = '+str(len(less_than_mean)))

# output:
# enter the numbers = 15000 26000 16000 19000 5000
# sum of numbers = 81000.0
# average of numbers = 81000.0/5 = 16200.0
# [15000.0, 16000.0, 5000.0]
# people with less than mean salary = 3

