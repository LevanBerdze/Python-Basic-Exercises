
import math   
def f(x):
    if x >= 0:
        return (1-x**2) * math.sin(math.pi*x)
        
    else:
        return (x**2 - 1) * math.sin(math.pi*x)
        
    

A = float(input('Enter A: '))
B = float(input('Enter B: '))
N = int(input('Enter N: '))



sum = 0   

delx = (B - A)/N 


for i in range(N+1):
    
    if i == 0:
        x = A + i * delx
        sum += f(x)
        
    elif i == N:
        x = A + i * delx
        sum += f(x)
        
    elif i % 2 == 1:
        x = A + i * delx
        sum += 4 * f(x)
        
    elif i % 2 == 0:
        x = A + i * delx
        sum += 2 * f(x)
        
        
 
integral = (delx/3) * sum 


print(f'{integral:.8f}')