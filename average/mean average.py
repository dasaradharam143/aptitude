def find_mean_average():
    no_of_denominations = list(map(float, input('enter denominations = ').split()))
    avg_of_values = list(map(float, input('enter values= ').split()))
    total = 0
    for i in range(len(no_of_denominations)):
        total += no_of_denominations[i] * avg_of_values[i]
    mean = total / sum(no_of_denominations)
    print('mean average = ' + str(total) + '/' + str(sum(no_of_denominations)) + ' = ' + str(round(mean, 5)))


def find_missing_number():
    no_of_denominations = list(map(float, input('enter denominations = ').split()))
    avg_of_values = list(map(float, input('enter values ( enter 0 inplace of x )= ').split()))
    index_0 = avg_of_values.index(0)
    average = int(input('average = '))
    total = 0
    for i in range(len(no_of_denominations)):
        total += no_of_denominations[i] * avg_of_values[i]
    missing_number = (average * sum(no_of_denominations) - total) / no_of_denominations[index_0]
    print('missing number = ' + str(round(missing_number, 4)))


condition = input('enter 1) to find mean average 2) to find missing number : ')
if condition == '1':
    find_mean_average()
elif condition == '2':
    find_missing_number()
else:
    print('enter a valid input')
