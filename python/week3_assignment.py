# Question 1
def calculate_discount(price, discount_percent): 
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price 


# Question 2
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price

# User input
price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount: "))

# Total price
final_price = calculate_discount(price, discount_percent)

# Print 
if discount_percent >= 20:
    print(f"total price after allowed discount: {final_price}")
else:
    print(f"Sorry, No discount. Original price: {price}")


