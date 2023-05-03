average_numbers = float(input("enter average of numbers = "))
n = int(input("enter number of outcomes = "))
total_sum = average_numbers * n
incorrect = list(map(int, input('incorrect values = ').split()))
correct = list(map(int, input('correct values = ').split()))
correct_total = total_sum - sum(incorrect) + sum(correct)
correct_average = correct_total / n
print('correct total = ' + str(total_sum) + ' - ' + str(sum(incorrect)) + ' + ' + str(sum(correct)))
print('correct average = ' + str(correct_total) + '/' + str(n) + ' = ' + str(round(correct_average, 2)))
