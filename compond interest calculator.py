import math

a = int(input('enter monthly investment = '))
months = int(input('enter no of months = '))
interest = float(input('enter rate of interest = '))
total = 0
for i in range(1, months + 1):
    sum1 = a * ((0.01 * interest + 1) ** i)
    total = total + sum1
    print(f'{i} months total = {math.ceil(total)}')
b = a * months
print(f'total amount for {months} months = {b}')
print(f'total interest for {months} months = {math.ceil(total - b)}')
