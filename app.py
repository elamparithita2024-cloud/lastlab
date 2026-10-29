def calculate_total(price, quantity):
    return price * quantity

def apply_discount(total, discount_percent):
    return total * (1 - (discount_percent / 100))

def main():
    print("=== Shopping Bill Calculator v2 (Discounts) ===")
    while True:
        print("\n1. Calculate Bill with Discount")
        print("2. Exit")
        choice = input("Enter choice (1-2): ")
        
        if choice == '1':
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                discount = float(input("Enter discount % (0-100): "))
                
                subtotal = calculate_total(price, quantity)
                final_total = apply_discount(subtotal, discount)
                
                print(f"Subtotal: ${subtotal:.2f} | Final: ${final_total:.2f}")
            except ValueError:
                print("Invalid input.")
        elif choice == '2':
            break
