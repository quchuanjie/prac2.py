"""
CP1404/CP5632 - Practical - Suggested Solution

"""

MINIMUN_LENGTH = 3


def version_1():
    password = input(f"Enter password of at leat {MINIMUN_LENGTH} characters:")
    while len(password)< MINIMUN_LENGTH:
        password = input(f"Enter password of at leat {MINIMUN_LENGTH} characters:")

    print('*'*len(password))

def main():
    password = input_password(MINIMUN_LENGTH)
    print_word(password)

def input_password(MINIUM_LENGTH):
    password = input(f"Enter password of at leat {MINIMUN_LENGTH} characters:")
    while len(password) < MINIUM_LENGTH:
        print("Password too short")
        password = input(f"Enter password of at leat {MINIMUN_LENGTH} characters:")
    return password

def print_word(password):
    print('*'*len(password))

main()
