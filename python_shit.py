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



# people = 10
# x = "There are {} types of people.".format(people)
#
# binary = "binary"
# do_not = "don't"
# y = f"Those who know {binary} and those who {do_not}."
#
# print(x)
# print(y)
#
# print("I said: {}".format(x))
# print(f"I also said: {y}.")
#
# hilarious = True
#
# joke_evaluation = "Isn't that joke so funny?!"
#
# print(joke_evaluation.format(hilarious))
#
# w = "This is the left side of..."
# e = "a string with a right side."

# # print(w + e)
#
# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"
#
# print(end1 +end2 + end3 + end4 + end5 + end6, end=" ")
# print(end7 + end8 + end9 + end10 + end11 + end12)
#
# formatter = "{} {} {} {}"
# time = 10
# distance = 12
# velocity = 8
# acceleration = 2
#
# print(formatter.format(1, 2, 3, 4))
# print(formatter.format(time, distance, velocity, acceleration))
# print(formatter.format("one", "two", "three", "four"))
# print(formatter.format(True, False, False, True))
# print(formatter.format(formatter, formatter, formatter, formatter))
# print(formatter.format("Try your own",
#     "text here",
#     "Maybe a Poem",
#     "or a song about fear"))
#
# days = "Mon \n Tue Wed Thu Fri Sat Sun"
# months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#
# print("Here are the days: ", days)
# print("Here are the months: ", months)
#
# print("""
# There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines is we want, or 5, or 6.
# """)

# tabby_cat = "\tI'm tabbed \tin"
# persian_cat = "I'm split\non a line"
# backlash_cat = "I'm \\ a \\ cat"
#
# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """
#
# random_cat = "If I enter wherever I want within these quotes, It will print\nas such?"
#
# print(tabby_cat)
# print(persian_cat)
# print(backlash_cat)
# print(fat_cat)
# print(random_cat)

# print("\njamf")
# print("N\{Lanice}")
#
# print('How old are you?', end=' ')
# age = input()
# print('How tall are you?', end= ' ')
# height = input()
# print('How much do you weigh?', end= ' ')
# weight = input()
#
# print("So, you're {} old, {} tall and {} heavy".format(age, height, weight))

# print("How old are you?"), input()


# from sys import argv
#
# script, first, second, third = argv
#
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)


# script, first = argv
# print("This is your script:", script)
# print("Here is the only variable:", first)

# word, name = argv

# print("Name of doc", word)
# print("What's your name?", name, input())
# # print("How old are you?", input())

from sys import argv

script, user_name = argv

prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me. You live in {lives}. Not sure where that is. And you have a {computer} type of computer. Nice.
""")
