#Shopping Cart

# Create a shopping cart programe that will continuously ask the user for a food productaand the price of that product
# Have an exit clause if the user wishes to stop adding more things to their
# At the end show the food items and total cost to the user

foods = []
prices = []
total = 0

while True:
    food = input('Enter a food for to buy or press q to quit')
    if food.lower == 'q':
        break
    else:
        price = float(input(f'Enter the price of the (food): R'))
        foods.append(food)
        prices.append(price)
        
print("-----YOUR CART-----")

for food in foods:
    print(food, end= " ")
    
for price in prices:
    total += price
    
print("\n")
print(f"your total is: R{total}")
        
        