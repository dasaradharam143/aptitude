numbers = list(map(float, input('enter the numbers = ').split()))
b = []
for i in numbers:
    b.append(round(1 / i, 5))
print(b)
avg = sum(b)/len(b)
print('average = '+str(sum(b))+'/'+str(len(b))+' = '+str(avg))
