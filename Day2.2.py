# print("Welcome to the tip calculator! ")

# total_bill = input("What was the total bill? ")
# tips = input("How much tip would you like to give? 10, 12, or 15? ")
# amount_people = input("How many people to split the bill? ")

# bill_with_tips = (float(tips) / 100 * int(total_bill) + int(total_bill))  # 12 + 100 = 112
# print(f"Total bill with tips: {bill_with_tips}")

# total_for_one = bill_with_tips / int(amount_people)
# print(total_for_one)



# Get inputs
total_bill = float(input("What was the total bill? $"))
tips = float(input("How much tip would you like to give? 10, 12, or 15? "))
amount_people = int(input("How many people to split the bill? "))

# Calculate total bill including tip
bill_with_tips = total_bill * (1 + tips / 100)
print(f"Total bill with tips: ${bill_with_tips:.2f}")

# Calculate amount per person
total_for_one = bill_with_tips / amount_people
print(f"Each person should pay: ${total_for_one:.2f}")