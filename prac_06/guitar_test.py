"""
Cp1404 practical
"""

from guitar import Guitar

current_year = 2022

def test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name,year,cost)
    other_guitar = Guitar("Another Guitar",2013)

    print(f"{guitar.name} get_age() - Expected {98}.Got {guitar.get_age()}")

    print(f"{other_guitar.name} get_age() - Expected {7}.Got {other_guitar.get_age()}")

    print()
    print(f"{guitar.name} is_vintage() - Expected {True}.Got {guitar.is_vintage()}")


    print(f"{other_guitar.name} is_vintage() - Expected {True}.Got {other_guitar.is_vintage()}")


if __name__ == '__main__':
    test()
