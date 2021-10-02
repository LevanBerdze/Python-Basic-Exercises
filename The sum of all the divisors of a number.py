#Write a function so that it returns the sum of all the divisors of a number, 
#without including it. A divisor is a number that divides into another 
#without a remainder.

def sum_divisors(n):
  total = 0
  x=1
  while x < n:
    if n % x == 0:
     total = total + x
     x = x+1
    else:
      x= x+1  
  return total 

n = int(input("Enter a number: "))
print(sum_divisors(n))
