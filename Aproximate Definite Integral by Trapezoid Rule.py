# Aproximate Definite Integral by Trapezoid Rule

import math   

def f(x):
     return math.sqrt(1+math.sin(x)**2)

A = float(input('Enter A: '))
B = float(input('Enter B: '))
N = int(input('Enter N: '))


sum = 0   

delx = (B - A)/N


for i in range(N+1):
    if i == 0:
        xi = A + i * delx
        sum += f(xi) 
    elif i == N:    
        xi = A + i * delx
        sum += f(xi)    
    else:
        xi = A + i * delx
        sum += (2 * f(xi))
       
     
integral = (delx/2) * sum  


print(f'{integral:.8f}')