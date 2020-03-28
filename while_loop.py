import sys


MASTER_PASS = "multi_pass"

password = input("please enter your password:  ")
attempt_count = 1
while password != MASTER_PASS:
    if attempt_count > 3:
        sys.exit("To many invalid attempts")
    password = input("invalid password please try again")
    attempt_count += 1
print("Welcome to funky town!")