def average_of_numbers():
    numbers = list(map(float, input('enter the numbers = ').split()))
    n = len(numbers)
    total = sum(numbers)
    average = total / n
    print('average of numbers = ' + str(round(average, 5)))


def missing_numbers():
    numbers = list(map(float, input('enter the numbers = ').split()))
    average = float(input('enter the average of total numbers = '))
    n = len(numbers) + 1
    total = sum(numbers)
    missing_number = (average * n) - total
    print('missing number = ' + str(missing_number))


def sum_of_total_numbers():
    average_numbers = int(input("enter average of numbers = "))
    n = int(input("enter number of outcomes = "))
    total_sum = average_numbers * n
    print(("total sum of numbers = " + str(total_sum)))


given_situation = input(
    'Enter the type of problem \na)average of numbers b)missing number c)total sum of numbers \nenter option: ').lower()
if given_situation == 'a':
    average_of_numbers()
elif given_situation == 'b':
    missing_numbers()
elif given_situation == 'c':
    sum_of_total_numbers()
else:
    print('enter a valid input')
