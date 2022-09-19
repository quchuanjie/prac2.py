"""
cp1404
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


MENU = "q)uit,c)hoose taxi,d)rive"

def main():
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Lets drive")
    print(MENU)
    choose_menu = input(">>>  ").lower()
    while choose_menu != 'q':
        if choose_menu == 'c':
            print("Taxis available: ")
            display_taxis(taxis)
            choose_taxi = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[choose_taxi]
            except IndexError:
                print("Invalid taxi choice")
        elif choose_menu == 'd':
            if current_taxi:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far?"))
                current_taxi.drive(drive_distance)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name,trip_cost))
                bill_to_date += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(bill_to_date))
        print(MENU)
        choose_menu = input(">>>  ").lower()

    print("Total trip cost: ${:.2f}".format(bill_to_date))
    print(MENU)
    display_taxis(taxis)


def display_taxis(taxis):
    for i,taxi in enumerate(taxis):
        print(f"{i} - {taxi}")



main()