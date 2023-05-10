def power_of_n(a, n):
    b = []
    for i in a:
        b.append(i ** n)
    return b


numbers = list(map(int, input('enter the numbers = ').split()))
power = int(input('enter the power of n = '))
total = power_of_n(numbers, power)
print('total = ' + str(total))
avg = sum(total) / len(total)
print('average = ' + str(sum(total)) + '/' + str(len(total)) + ' = ' + str(round(avg,5)))
