#Kevin
def liters_100km_to_miles_gallon(liters):
    miles_per_gallon = 100 / (liters / 3.785411784) * 0.621371
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    liters_per_100km = 100 / (miles / 0.621371) * 3.785411784
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
