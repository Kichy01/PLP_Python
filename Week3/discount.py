def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * (discount_percent / 100))
    
    else:
        return price 
    
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the percentage discount received: "))
    final_price = calculate_discount(price, discount_percent)

    if discount_percent >=20:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"No discount was applied: The final price is: {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values!")