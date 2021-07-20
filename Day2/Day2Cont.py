# This is a mini challenge on control flow statements
# Here in this challenge we will give a list of options and print appropriate messages
while True:
    print("1. Learn Java\n2. Learn Python\n3.Do a thirty day challenge\n4.Do a 100 day challenge\n0.Exit")
    option = int(input("Enter your option:"))
    if option == 1:
        print("You have selected option {}. Learn Java".format(option))
    elif option == 2:
        print("You have selected option {}. Learn Python".format(option))
    elif option == 3:
        print("You have selected option {}. Do a thirty day challenge".format(option))
    elif option == 4:
        print("You have selected option {}. Do a 100 day challenge".format(option))
    elif option == 0:
        break
    else:
        continue
