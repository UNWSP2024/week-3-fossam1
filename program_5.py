# Samuel Foss
# Program 5 Hot Dog
# 9/18/2024

# There are two kinds of hot dogs sold:
# Hot Dog ($3.50), Chili Dog ($4.50).
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).
# Also tax is 7%.
# Write a program the inputs the type of hot dog wanted and optional toppings.
# The program then displays the hot dog cost, tax and total cost.

price = 0.00

hotdog = input("Would you like a hotdog or chilidog? : ").lower()
if hotdog == "hotdog" : price += 3.50
if hotdog == "chilidog" : price += 4.50
cheese = input("Would you like Cheese? : ").lower()
if cheese == "yes" : price += 0.50
peppers = input("Would you like Peppers? : ").lower()
if peppers == "yes" : price += 0.75
onions = input("Would you like Grilled Onions? : ").lower()
if onions == "yes" : price += 1.00

tax = 0.07 * price
totalcost = tax + price
print(f"cost: ${price:.2f}")
print(f"tax: ${tax:.2f}")
print(f"totalcost: ${totalcost:.2f}")

#Output
#Would you like a hotdog or chilidog? : HOTDOG
#Would you like Cheese? : NO
#Would you like Peppers? : YeS
#Would you like Grilled Onions? : Yes
#cost: $5.25
#tax: $0.37
#totalcost: $5.62

#Process finished with exit code 0
