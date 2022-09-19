import random

Numbers_Line = 6
MINnumber = 1
MAXnumber = 45

def main():
    enter_numbers = int(input("How many quick picks?"))
    while enter_numbers < 0:
        print("Invalid numbers!")
        enter_numbers = int(input("How many quick picks?"))

    for i in range(enter_numbers):
        quick_pick = []
        for j in range(Numbers_Line):
             number = random.randint(MINnumber,MAXnumber)
             while number in quick_pick:
                   number = random.randint(MINnumber,MAXnumber)
             quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()