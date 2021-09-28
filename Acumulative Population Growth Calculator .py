import math
p = float(input("Enter initial population: "))
t = float(input("Enter first time period in years:  "))
r = (float(input("Enter first growth rate: ")) / 100)
def pop_growth(p,t,r):
    return p*math.e**(r*t)

p = pop_growth(p,t,r)

t = float(input("Enter second time period in years:  "))
r = (float(input("Entrt second growth rate: ")) / 100)

p = pop_growth(p,t,r)

t = float(input("Enter third time period in years:  "))
r = (float(input("Entrt third growth rate: ")) / 100)


print(f'Final Population is {pop_growth(p,t,r)}')

