def average_of_numbers():
    numbers = list(map(float, input('enter the numbers = ').split()))
    n = len(numbers)
    total = sum(numbers)
    average = total / n
    print('sum of numbers = ' + str(total))
    print('average of numbers = ' + str(total) + '/' + str(n) + ' = ' + str(round(average, 5)))


def missing_numbers():
    numbers = list(map(float, input('enter the numbers = ').split()))
    average = float(input('enter the average of total numbers = '))
    n = len(numbers) + 1
    total = sum(numbers)
    missing_number = (average * n) - total
    print('sum of numbers = ' + str(total) + '\nsum of total numbers = ' + str(average * n))
    print('missing number = ' + str(average * n) + ' - ' + str(total) + ' = ' + str(missing_number))


def sum_of_total_numbers():
    average_numbers = int(input("enter average of numbers = "))
    n = int(input("enter number of outcomes = "))
    total_sum = average_numbers * n
    print(("total sum of numbers = " + str(total_sum)))


def missing_numbers_case1():
    total_average = float(input('enter the average of total numbers = '))
    average_numbers = float(input("enter the average of numbers = "))
    total_numbers = int(input('total outcomes = '))
    sum_of_numbers = average_numbers * (total_numbers - 1)
    missing_number = total_numbers * total_average - sum_of_numbers
    print('sum of numbers = ' + str(sum_of_numbers) + '\nsum of total numbers = ' + str(total_numbers * total_average))
    print('missing number = ' + str(missing_number))


given_situation = input(
    'Enter the type of problem \na)average of numbers b)missing number \nc)total sum of numbers d)missing number '
    'using average \nenter option: ').lower()
if given_situation == 'a':
    average_of_numbers()
elif given_situation == 'b':
    missing_numbers()
elif given_situation == 'c':
    sum_of_total_numbers()
elif given_situation == 'd':
    missing_numbers_case1()
else:
    print('enter a valid input')
