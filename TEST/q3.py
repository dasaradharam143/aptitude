a=int(input('no of people = '))
b=int(input('no of people paid = '))
c=int(input('average of amount spent by people = '))
d=int(input('amount paid extra by n th person = '))
formula  = ( b * c + d)/(a-1)
print('amount spent by nth person = ' +str(formula))
total = a*formula
print('total amount spent bt them = '+str(total))

#
# output:
# no of people = 9
# no of people paid = 8
# average of amount spent by people = 30
# amount paid extra by n th person = 20
# amount spent by nth person = 32.5
# total amount spent bt them = 292.5