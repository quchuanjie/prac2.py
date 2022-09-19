"""
cp1404 car test
"""

from prac_08.unreliable_car import UnreliableCar

def main():
    # Create different cars
    good_car = UnreliableCar("Good", 100, 80)
    bad_car = UnreliableCar("Trash Car", 100, 19)


    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    # print the final states of the cars
    print(good_car)
    print(bad_car)


main()