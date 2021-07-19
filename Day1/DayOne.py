# From today I am starting a 30 day journey of revising python for 30 days
# Day1
# Making a Hello World File as always, playing with variables and
# arithmetic operators and some string formatting

print("Hello World")
a = int(input("Enter a number: "))
b = int(input("Enter the next number: "))
print("Sum: ", a + b)
print("Difference: ", a - b)
print("Product: ", a * b)
print("Remainder: ", a % b)
print("Division of a/b", a/b)

person_name = input("Enter your name: ")
print("Hello {}".format(person_name))
age = int(input("Enter your age: "))
print("Hello {0} and you are {1} years old".format(person_name, age))

# String formatting using f-strings

print(f'Hello {person_name}')
print(f'You have entered {age} as your age')
