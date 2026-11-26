
customer_name = input("Enter customer name: ")
customer_age = int(input("Enter customer age: "))

while True:
    membership_response = input("Are you a member? (True/False): ")
    if membership_response in ("true", "false"):
        membership_status = membership_response == "true"
        break
    print("Please enter True or False")

no_of_products = int(input("Enter the number of products purchased: "))

price_list = [33, 45, 12, 67, 56]
product_names = ("Product A", "Product B", "Product C", "Product D","Product E")
products = dict(zip(product_names, price_list))

print("\nCustomer information")
print("Name:", {customer_name})
print("age:", {customer_age})
print("Membership status:", {membership_status})
print("Number of products purchased:", {no_of_products})

print("\n Available products and prices")
for product_name, price in products.items():
    print(f"{product_name}:, {price:.2f}")

averageprice = sum(price_list) / len(price_list)
highest_priced_product = max(products, key=products.get)
lowest_pricedproduct = min(products, key=products.get)

print(f"\n Average product price: {averageprice:.2f}")
print(f"Highest-priced product: {highest_priced_product} ",f"({products[highest_priced_product]:.2f})")

print(f"Lowest-priced product: {lowest_pricedproduct} ",f"({products[lowest_pricedproduct]:.2f})")