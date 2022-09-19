def main():
    name_email = {}
    email = input("Email:")
    while email != "":
        name = get_name_for_email(email)
        Ask = input("Is your name {}?(Y/N)".format(name) )
        if Ask.upper() != "Y" and Ask != "":
            name = input("Name: ")
        name_email[email] = name
        email = input("Email:")

    for email,name in name_email.items():
        print("{}({})".format(name,email))

def get_name_for_email(email):
     front = email.split('@')[0]
     parts = front.split('.')
     name = " ".join(parts).title()
     return name



main()
