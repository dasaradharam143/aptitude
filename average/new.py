a=int(input('distance = '))
b=int(input('a beats by b distance = '))
c=a-b
print(c)
d=int(input('time differnce = '))
e=float(input('a bets b by time = '))

t = (d*a - c*e) /(c-a)
print(t)
aspeed = a/t
bspeed = c/(t+d)
print(aspeed)
print(bspeed)
