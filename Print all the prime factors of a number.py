# Write the print_prime_factors function print and
#all the prime factors of a number.

def print_prime_factors(number):
 
  factor = 2
  while factor <= number:
   
    if number % factor == 0:
      print(factor)
      number = number / factor
    else:
      
      factor +=1
  return "Done"

print_prime_factors(int(input("Type number you want see prime factor of: ? ")))