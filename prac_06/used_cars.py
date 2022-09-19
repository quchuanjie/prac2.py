"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My car",180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("Limo", 100)

    limo.add_fuel(20)

    print(f"Fuel in limo:{limo.fuel}")

    distance_drive = limo.drive(115)

    print(f"Limo Odometer:{limo.odometer}")
    print(f"Tried driving 115km.Actual distance traveled:{distance_drive}")

    distance_drive = limo.drive(120)
    print(f"Limo Odometer:{limo.odometer}")
    print(f"Tried driving 100km.Actual distance traveled:{distance_drive}")

    print(f"limo,fuel={limo.fuel},odometer={limo.odometer}")




main()