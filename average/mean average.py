no_of_denominations = list(map(float, input('enter denominations = ').split()))
avg_of_values = list(map(float, input('enter values= ').split()))
total = 0
for i in range(len(no_of_denominations)):
    total += no_of_denominations[i] * avg_of_values[i]
mean = total / sum(no_of_denominations)
print('mean average = '+str(total)+'/'+str(sum(no_of_denominations))+' = '+str(round(mean, 5)))
