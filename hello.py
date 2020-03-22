msg1 = "Hello World"
firstName = "Allen"
favorite_color = "plaid"
msg2 = "is learning Python"
msg1.capitalize
print(msg1)


# print(msg1, firstName, msg2, "his favorite color is", favorite_color)

# lastName = input("What is your last name?")

# print("Hello", firstName, lastName)

# quest = input("what is your quest")

# print("Well", firstName, lastName, "i bid you good luck on your quest to", quest)

# PEMDAS = "please excuse my dear aunt sally"

# print("Well", firstName, lastName, "\ni bid you good luck on your quest to", quest)

print(favorite_color*20)

#len stands for length
print(len(favorite_color*20))

print(favorite_color.upper())

print(msg1.title())

subject_template = "thanks for learning {} with us {}"

print(subject_template.format("python", firstName))

