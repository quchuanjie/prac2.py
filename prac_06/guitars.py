"""
cp1404 practical
"""
from guitar import Guitar

def main():
    guitars=[]

    print("My guitars!")
    name = input("Name:")
    while name != "":
        year = int(input("Year:"))
        cost = float(input("Cost:"))
        guitar_add = Guitar(name,year,cost)
        guitars.append(guitar_add)
        print(guitar_add,"added.")
        name = input("Name:")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i,guitars in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitar :")

main()


