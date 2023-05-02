a = list(map(float, input('enter the numbers = ').split()))
b = []
for i in a:
    b.append(round(1 / i,5))
avg = sum(b)/len(b)
print('average = '+str(avg))

