#Complete the function to return the result of the conversion
#Call the function to convert the trip distance from miles to kilometers
#Fill in the blank to print the result of the conversion
#Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result

def convert_distance(miles):
	return miles * 1.6  

my_trip_miles = 55
my_trip_km = convert_distance(55)
round_trip_km = my_trip_km * 2

print("The distance in kilometers is " , my_trip_km)
print("The round-trip in kilometers is ", round_trip_km)