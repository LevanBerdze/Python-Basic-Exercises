# Calculate the round-trip in kilometers by doubling the result
# 1) create the function to return the result of the conversion
# 2) Convert my_trip_miles to kilometers by calling the function above and print the result of the conversion
# 3) Calculate the round-trip in kilometers by doubling the result

def convert_distance(miles):
	return miles * 1.6  

my_trip_miles = 55
my_trip_km = convert_distance(55)
round_trip_km = my_trip_km * 2

print("The distance in kilometers is " , my_trip_km)
print("The round-trip in kilometers is ", round_trip_km)