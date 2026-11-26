

Products = {"Product A": 33,"Product B": 45,"Product C": 12,"Product D": 67,"Product E": 56}

def display_products(products):
    print("\n Available Products")
    for product_name, price in products.items():
        print(f"{product_name}: {price:}")


def add_to_cart(products, cart):
    print("Add a selected product and quantity to the cart.")
    while True:
        product_name = input("\n Enter a product name to add : ")
        if product_name.lower() == "done":
            break
        if product_name not in products:
            print("That product is not available.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {product_name}: "))
        except ValueError:
            print("Please enter a wholenumber quantity.")
            continue
        if quantity <= 0:
            print("Quantity mustbe greater than zero.")
            continue

        cart[product_name] = cart.get(product_name, 0) + quantity
        print(f"Added {quantity} of {product_name} to the cart.")

    return cart


def view_cart(cart, products):
    
    print("Display selected products and quanties and return the subtotal.")
    print("\n Your cart:")
    if not cart:
        print("The cart is EMPTY.")
        return 0.0

    subtotal = 0.0
    for product_name, quantity in cart.items():
        item_total = products[product_name] * quantity
        subtotal += item_total
        print(f"{product_name}: {quantity} x {products[product_name]}", f" = {item_total}")
    print(f"Subtotal: {subtotal:.2f}")
    return subtotal


def calculate_bill(cart, products):
    
    return sum(products[product_name] * quantity
               for product_name, quantity in cart.items())


def apply_discount(total):

    if total < 500:
        discount_rate = 0.0
    elif total < 1000:
        discount_rate = 0.05
    elif total < 2000:
        discount_rate = 0.10
    else:
        discount_rate = 0.15

    discount = total * discount_rate
    return discount, total - discount


def main():
    cart = {}
    display_products(Products)
    add_to_cart(Products, cart)
    view_cart(cart, Products)

    subtotal = calculate_bill(cart, Products)
    discount, final_total = apply_discount(subtotal)
    print("\n Final bill:")
    print(f"Subtotal: {subtotal}")
    print(f"Discount: {discount}")
    print(f"Total after discount: {final_total}")


if __name__ == "__main__":
    main()