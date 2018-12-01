# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven
#
#
# print("There are", cars, "cars available.")
# print("There are {} cars available".format(cars))
# print("There are only {} drivers available".format(drivers))
# print("There will be {} empty cars today".format(cars_not_driven))
# print("We can transport {} people today because there are {} drivers".format(carpool_capacity, drivers))

# name = 'Zed A. Shaw'
# age = 20
# height = 72
# weight = 180
# eyes = 'Blue'
# teeth = 'White'
# hair = 'Brown'
# height_in_cent = height * 2.54
# weight_in_kilo = weight / 2.2
#
# print(f"Let's talk about {name}.")
# print("Let's talk about {}.".format(name))
# print(f"He's {height} inches tall and {weight} pounds.")
# print("He's got {} eyes, {} hair, and {} teeth, which is preferred.".format(eyes, hair, teeth))
#
# total = age + height + weight
# print("If I add {}, {}, and {}, I get {}.".format(age, height, weight, total))
#
# print("If I add {}, {}, and {}, I get {}.".format(age, height_in_cent, weight_in_kilo, total))



people = 10
x = "There are {} types of people.".format(people)

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print("I said: {}".format(x))
print(f"I also said: {y}.")

hilarious = True

joke_evaluation = "Isn't that joke so funny?!"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
