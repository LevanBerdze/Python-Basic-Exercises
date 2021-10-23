
a = float(input("Enter x^2 coefficient: "))  
b = float(input("Enter x^1 coefficient: ")) 
c = float(input("Enter x^0 coefficient: "))  



def quadratic_equation (a1, b1, c1): #defining equation
    disc = b1**2 - 4*a1*c1
    sqrt_of_disc = ( disc**(1/2) )
    form_part_1 = -b1/(2*a1)         #real partt of equation
    
    if disc == 0:
        print(f'ONE SOLUTION: x = {form_part_1:.4f}')
    elif disc > 0:
        real_sol_1 = (form_part_1 + (sqrt_of_disc/(2*a1)))
        real_sol_2 = (form_part_1 - (sqrt_of_disc/(2*a1)))
        print(f'TWO REAL SOLUTIONS: x = {real_sol_1:.4f} and x = {real_sol_2:.4f}')
    else:        
        abs_val_disc = (-1 )* disc
        imaginary_part = ( (abs_val_disc)**(1/2) ) / ( 2*a1)     
        print(f'COMPLEX SOLUTIONS: x = {form_part_1:.4f} - {imaginary_part:.4f}i and x = {form_part_1:.4f} + {imaginary_part:.4f}i')
    
              
              
                
                  
if a == 0:
    if  b == 0 and c == 0: 
        print("Infinitely Many Solutions \nThe graph lies on X-axes")
    elif b == 0: 
        print("NO SOLUTION \nThe graph is horizontal line and never cross X-axes")
    else:
        lin_sol = c/-b
        print(f'ONE SOLUTION: x = {lin_sol:.4f}')
else:
   quadratic_equation(a,b,c)
    
    

