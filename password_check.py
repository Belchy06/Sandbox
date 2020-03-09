min_length = 5


def valid_password(user_input):
    return len(user_input) >= min_length


password = input("Please enter a password: ")
while not valid_password(password):
    password = input("Please enter a password longer than {} characters: ".format(min_length))

for char in password:
    print("*", end="")
