input_1 = int(input("Enter number: "))
input_2 = int(input("Enter another number: "))

if input_1 > input_2:
    lo = input_2
    hi = input_1
elif input_1 < input_2:
    lo = input_1
    hi = input_2
else:
    print("Please, Do not enter the same number")
    input_1 = int(input("Enter number: "))
    input_2 = int(input("Enter another number: "))
i = 1
result = lo
while (lo+i) <= hi:
	result += (lo+i)
	i += 1
print(result)    