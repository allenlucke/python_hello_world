import math

# def split_the_bill(total, num_ppl):
#     return math.ceil(total / num_ppl)

# total_due = float(input("What is the total?"))
# num_ppl = int(input("How many people?"))

# each_share = split_the_bill(total_due, num_ppl)

# print("We each owe ${}".format(math.ceil(each_share)))


# def square(number):
#     return(number*number)

# result = square(5)


# print(result)
# print(square(5))

def split_the_bill(total, num_ppl):
    if num_ppl <= 1:
        raise ValueError("More than one person is required to split")
    return math.ceil(total / num_ppl)

try:
    total_due = float(input("What is the total?"))
    num_ppl = int(input("How many people?"))
    each_share = split_the_bill(total_due, num_ppl)

    print("We each owe ${}".format(math.ceil(each_share)))
except ValueError as err:
    print("Oh no that's not a number, try again")
    print('{}'.format(err))


# each_share = split_the_bill(total_due, num_ppl)

# print("We each owe ${}".format(math.ceil(each_share)))
