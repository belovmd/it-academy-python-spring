import glob
import re
import sys
from time import localtime

# output
print("Hello, world!")

# input, assigment
name = input("What is your name?\n")
print("Hi, %s." % name)

# for loop, built-in enumerate function, new style formatting
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# Fibonacci, tuple assignment
parents, babies = (1, 1)
while babies < 100:
    print("This generation has {0} babues".format(babies))
    parents, babies = (babies, parents + babies)


# Functions
def greet(name):
    print('Hello', name)


greet("Jack")
greet("Sill")
greet("Bob")

# import, regular expressions
for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, "is a valid US local phone number")
    else:
        print(test_string, "rejected")

# Dictionaries, generator expressions
prices = {"apple": 0.40, "banana": 0.50}
my_purchase = {
    "apple": 1,
    "banana": 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print("I owe the grocer $%.2f" % grocery_bill)

# Command line arguments, exception handing
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print("sum = ", total)
except ValueError:
    print("Please supply integer arguments")
# Opening files
python_Files = glob.glob("*.py")
for file_name in sorted(python_Files):
    print("   ------" + file_name)

    with open(file_name) as f:
        for line in f:
            print("   " + line.rstrip())
    print()

# Time, conditionals, from, import, for...else
activities = {8: "Sleeping",
              9: "Commuting",
              17: "Working",
              18: "Commuting",
              20: "Eating",
              22: "Reating"}

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print(activities[activity_time])
        break
else:
    print("Unknown, AFK or sleeping")
