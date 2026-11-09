
# 1. I would use .get() when I am not sure if a key exists because it stops errors.
#2. This reminds me of using a pivot table in excel to group and add up information.
# python can be more useful for large datasets because it can process information and handle more.

print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250
}




print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


print("--- Exercise 2 ---")
customer["phone"] = "123-456-7890"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print(customer.get("email", "email not found"))


print("--- Exercise 3 ---")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError caught: {error}")


print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for item in customer:
    print(item)


print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0,
                  "silver": 0.05,
                  "gold": 0.10,
                  "platinum": 0.15}
purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"tier: {customer['tier']}")
print(f"discount: {discount_rate * 100:.0f}%")
print(f"final price: ${final_price:.2f}")


print("--- Exercise 6 ---")

customers = [
    {"name": "bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "david", "tier": "bronze", "ytd_spend": 450}
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on $300 purchase")


print("--- Exercise 7 ---")
catalog = {
    "widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] <20:
        print(f"Low Stock: {product} - Only {details['stock']} left in stock!")


print("--- Exercise 8 ---")
transactions = [
    {"region": "south", "amount": 300},
    {"region": "north", "amount": 150},
    {"region": "south", "amount": 200}
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
    print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]}")

