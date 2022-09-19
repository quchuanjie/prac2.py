total_price = 0
number = int(input("Number of items:"))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))
for i in range(number):
    Price = float(input("Price of item: "))
    total_price += Price
if total_price > 100:
    total_price = total_price-(total_price*0.1)
    print(f"Total price for {number} items is ${total_price}")
else:
    print(f"Total price for {number} items is ${total_price}")

