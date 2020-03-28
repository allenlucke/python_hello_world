statement = "It's a beautiful day"
statement = statement.upper()
num_char = len(statement)
result = statement + "!" * num_char
print(result)

questions = "Don't forget to ask for help"
questions = questions.upper()
num_char = len(questions)
result = questions + '!' * num_char
print(result)

# def = define

def hey(text):
    text = text.upper()
    num_char = len(text)
    result = text + "!" * num_char
    print(result)

hey('hey people')

hey("first python function being used here")