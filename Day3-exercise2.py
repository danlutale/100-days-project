print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni in your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0
# todo: work out how much they have to pay based on their size choises.
# todo: work out how much to add to their bill baseed on their pepperoni choises.
# todo: work out their final amount based on whether if they want extra cheese. 

if size == "S":
    price += 15
    if pepperoni == "Y":
        price += 2
elif size == "M":
    price += 20
    if pepperoni == "Y":
        price += 3
elif size == "L":
    price += 25
    if pepperoni == "Y":
        price += 3

else:
    print("Invalid size selected.")
    exit()

if extra_cheese == "Y":
    price += 1

print(f"The price of your pizza is ${price}.")