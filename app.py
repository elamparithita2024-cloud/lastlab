def calculate_total(price, quantity):
    return price * quantity

def main():
    print("=== Shopping Bill Calculator ===")
    while True:
        print("\n1. Calculate Bill")
        print("2. Exit")
        choice = input("Enter choice (1-2): ")
        
        if choice == '1':
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                if price < 0 or quantity < 0:
                    print("Price and quantity must be positive.")
                    continue
                
                total = calculate_total(price, quantity)
                print(f"Total Bill: ${total:.2f}")
            except ValueError:
                print("Invalid input! Enter numbers only.")
        elif choice == '2':
            print("Goodbye!")
            break
