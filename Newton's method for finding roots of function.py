#******************************************************************************
# newton.py
#******************************************************************************
# Name: 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#


def poly_deriv(polylist):
    '''
     Parameters
    ----------
    polylist : a nonempty list that contains floats corresponding to the 
    coefficients of a polynomial, starting with lower order coefficients

    Returns
    -------
    derivlist : list that contains floats corresponding to the coefficients of 
    the derivative of the input polynomial, starting with lower order coefficients
    '''
    ########### INSERT YOUR CODE HERE #############
    derivlist = []
    for i in range(len(polylist)):
        if i == 0:
            pass
        else:
            derivlist.append(i * polylist[i])
       

    return derivlist



def poly_eval(polylist, x):
    '''
    Parameters
    ----------
    polylist : a nonempty list that contains floats corresponding to the 
    coefficients of a polynomial, starting with lower order coefficients
    x : float corresponding to the input to the polynomial

    Returns
    -------
    value : float corresponding to the output of the polynomial evaluated at x
    '''
    ########### INSERT YOUR CODE HERE #############
    value = 0
    for i in range(len(polylist)):
        value+=polylist[i] * x**i
    
    
    return value

def main():
    
    coeflist = [] # initializes the coeffient list

    for i in range(8): # gets input for coefficients c0, c1, c2, c3, c4, c5, c6, c7
        c = float(input(f'Enter x^{i} coefficient: '))
        coeflist.append(c)
        
    # gets rid of any extraneous entries in the list
    while coeflist[- 1] == 0: 
        del coeflist[- 1]
    
    guess = float(input('Enter guess: ')) # the initial guess for Newton's method
    
    # the number of iterations for Newton'n method
    iterations = int(input('Enter number of iterations of Newton\'s method: '))

    # INSERT CODE FOR NEWTON'S METHOD HERE. YOUR CODE SHOULD USE THE FUNCTIONS
    # poly_deriv and poly_eval which you write the code for above
    
    
    for i in range(1,iterations+1):
        
        guess = guess - (poly_eval(coeflist ,guess) / poly_eval(poly_deriv(coeflist),guess))
        
    return guess
    

print(main()) 