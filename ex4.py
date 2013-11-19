cars = 100
space_in_a_car = 4.0
driver = 30
passengers = 90
cars_not_driven = cars - driver
cars_driven = driver
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", driver, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#stupid syntax is such a pain sometimes
#This exercise taught me that you dont have to use long variable names
#I can easily replace space_in_cars with the word space and it would work just fine.
#also I learned that using variable names to define what your working with is a lot better then using letters x.y/z
