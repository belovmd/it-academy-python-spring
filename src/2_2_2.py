"""In this mission you should write a function that
introduces a person with the given parameter's attributes.
Input: Two arguments. String and positive integer.
Output: String.
Example:

say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"""


def introduce(name: str, age: int) -> str:
    return "Hi. My name is {name} " \
           "and I'm {age} years old".format(age=age, name=name)


f = introduce(name=str(input("Insert Name: ")), age=int(input("Insert age: ")))
print(f)
