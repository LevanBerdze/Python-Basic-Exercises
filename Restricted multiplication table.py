#The multiplication_table function prints the results of a number passed to it
#multiplied by 1 through 5. An additional requirement is that the result 
#is not to exceed 25

def multiplication_table(number):
	
	multiplier = 1
	
	while multiplier <= 5:
		result = number * multiplier
		
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		
		multiplier += 1

number = int(input("Enter a number: "))
print(multiplication_table(number))
