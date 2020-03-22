# function to see if mo is in mother
has_mo = "mo" in "mother"

# print(has_mo)

# print(not True)

# print(True and True)

# print(True and False)

# print(True or False)

fruit = "apples"
print(fruit == "oranges")

firstName = input("What is your first name?")


if firstName == "Allen":
     print("hello,", firstName)
elif(firstName == "Andrea"):
    print("yay it's {}".format(firstName))
else:
    age = int(input("How old are you?"))
    if age > 10:
        print("Since you are {} years old, Would you like to try some python, {}?".format(age, firstName))
    print("Where is Allen?")

print("Have a great day {}".format(firstName))