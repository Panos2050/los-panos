def calculate_total_cost(price, quantity):
    return price * quantity

price = int(input("Please enter price: \n"))
quantity = int(input("Please enter quantity: \n"))
while True:
    try:
        discount = int(input("Please enter the discout presentage please.\n"))
        if 0 <= discount <= 100:
            break
        else:
            print("Please enter a valid percentage between 0 and 100.")
    except ValueError:
        print("Please enter a valid value.")
total = calculate_total_cost(price, quantity)
total_amount= total * (discount / 100)
total_cost = total - total_amount
print(f"The total cost for {quantity} items at {price} is {total} euros, but after the {discount}% discount is {total_cost:.2f} euros.")
# Just testing Git commit.
# Just testing Git commit.

