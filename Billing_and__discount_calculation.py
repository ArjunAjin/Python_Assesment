

Products = {"Product A": 33.00,"Product B": 45.00,"Product C": 12.00,"Product D": 67.00,"Product E": 56.00,}

def main():
    quantities = {}

    print("Available products:")
    for product_name, price in Products.items():
        print(f"{product_name}: {price:.2f}")

    print("\nEnter 0 for any product you do not want.")
    for product_name in Products:
        while True:
            try:
                quantity = int(input(f"Quantity of {product_name}: "))
                if quantity >= 0:
                    quantities[product_name] = quantity
                    break
                print("Quantity cannot be negative.")
            except ValueError:
                print("Please enter a whole number.")

    while True:
        membership_response = input("\nAre you a member? (yes/no): ").strip().lower()
        if membership_response in ("yes", "no"):
            is_member = membership_response == "yes"
            break
        print("Please enter yes or no.")

    selected_products = {product_name: quantity 
    for product_name, quantity in quantities.items()
        if quantity > 0}

    print("\n Selected products")
    subtotal = 0.0
    if selected_products:
        for product_name, quantity in selected_products.items():
            item_total = Products[product_name] * quantity
            subtotal += item_total
            print(
                f"{product_name}: {quantity} X ",f"{Products[product_name]:.2f} = {item_total:.2f}")
    else:
        print("No products selected.")

    if subtotal < 500:
        discount_rate = 0.0
    elif subtotal < 1000:
        discount_rate = 0.5
    elif subtotal < 2000:
        discount_rate = 0.10
    else:
        discount_rate = 0.15

    first_discount = subtotal * discount_rate
    amount_after_first_discount = subtotal - first_discount
    member_discount = amount_after_first_discount * 0.05 if is_member else 0.0
    final_total = amount_after_first_discount - member_discount

    print("\n FINAL BILL")
    print(f"Total: {subtotal:.2f}")
    print(f"Discount ({discount_rate:.0%}): {first_discount:.2f}")
    print(f"Member discount: -{member_discount:.2f}")
    print(f"Total bill: {final_total:.2f}")


if __name__ == "__main__":
    main()