orders = [
    ("Ravi", "Laptop", "Electronics", 55000),
    ("Anita", "T-Shirt", "Clothing", 1200),
    ("Ravi", "Mouse", "Electronics", 800),
    ("Sita", "Mixer", "Home Essentials", 3000),
    ("Anita", "Jeans", "Clothing", 2000),
    ("Ravi", "Keyboard", "Electronics", 1500),
    ("Sita", "Bedsheet", "Home Essentials", 1800),
    ("Kiran", "Shirt", "Clothing", 1500),
    ("Kiran", "Bottle", "Home Essentials", 500),
    ("Anita", "Headphones", "Electronics", 2500)
]

#Requirement1:
#Creating a dictionary 'customer_product_history' where keys are customer names and values are lists of ordered products.
#customer_product_history = {'Ravi': ['Laptop', 'Mouse', 'Keyboard'], 'Anita': ['T-Shirt', 'Jeans', 'Headphones'], 'Sita': ['Mixer', 'Bedsheet'], 'Kiran': ['Shirt', 'Bottle']}
customer_product_history = {}

#Requirement2:
#Dictionary 'Product_Mapping_Catagory' to map each product to its category.
#Product_Mapping_Catagory = {'Electronics': ['Laptop', 'Mouse', 'Keyboard', 'Headphones'], 'Clothing': ['T-Shirt', 'Jeans', 'Shirt'], 'Home Essentials': ['Mixer', 'Bedsheet', 'Bottle']}
#Create a set of unique product categories and display them.
Product_Mapping_Catagory = {}

#Requirement3:
#Dictionary 'customer_total_spent' to calculate the total amount spent by each customer.
#customer_total_spent = {'Ravi': 57300, 'Anita': 5700, 'Sita': 4800, 'Kiran': 2000}
#Based on the total spending I divided customers into three groups
#High Value customers who spent the most.
#Moderate buyers.
#Low Value customers.
customer_total_spent = {}

#Requirement4:
#Calculate total revenue for each product category.
# Total_Revenue_each_product = {'Electronics': 59800, 'Clothing': 4700, 'Home Essentials': 5300}
Total_Revenue_each_product = {}
#Set to store all unique products ordered
all_unique_products = set()

#Requirement5:
#Print a summary of each customer’s total spending and their classification
customer_total_spent_classification = {}

for order in orders:
    customer = order[0]
    product = order[1]
    category = order[2]
    price = order[3]

    #Requirement1:
    if customer not in customer_product_history:
        customer_product_history[customer] = [product]
    else:
        customer_product_history[customer].append(product)

    #Requirement2:
    if category not in Product_Mapping_Catagory:
        Product_Mapping_Catagory[category] = [product]
    else:
        Product_Mapping_Catagory[category].append(product)

    #Requirement3:
    if customer not in customer_total_spent:
        customer_total_spent[customer] = price
    else:
        customer_total_spent[customer] += price

    #Requirement4:
    if category not in Total_Revenue_each_product:
        Total_Revenue_each_product[category] = price
    else:
        Total_Revenue_each_product[category] += price
    #Add product to unique products set
    all_unique_products.add(product)


print("Requirement1:Customer Product History:", customer_product_history)
print()
print("Requirement2:Product Mapping Category:", Product_Mapping_Catagory)
print("Requirement2:Create a set of unique product categories & display them:", set(Product_Mapping_Catagory.keys()))
print(type(set(Product_Mapping_Catagory.keys())))
print()
print("Requirement3:Customer Total Spent:", customer_total_spent)
print("Requirement3:Based on the total spending I divided customers into three groups" )
for customer, total_spent in customer_total_spent.items():
    if total_spent >= 6000:
        print(customer, "is a High Value Customer.")
        customer_total_spent_classification[customer] = [total_spent,"High Value Customer"]
    elif 5000 <= total_spent < 6000:
        print(customer, "is a Moderate Buyer.")
        customer_total_spent_classification[customer] = [total_spent,"is a Moderate Buyer"]
    else:
        print(customer, "is a Low Value Customer.")
        customer_total_spent_classification[customer] = [total_spent,"is a Low Value Customer"]
print()
print("Requirement4:Total Revenue Each Product Category:", Total_Revenue_each_product)
# Found all unique products ordered
print("Requirement4: All Unique Products Ordered:", all_unique_products)
# Identified customers who bought only Electronics using list comprehension.
#Product_Mapping_Catagory = {'Electronics': ['Laptop', 'Mouse', 'Keyboard', 'Headphones'], 'Clothing': ['T-Shirt', 'Jeans', 'Shirt'], 'Home Essentials': ['Mixer', 'Bedsheet', 'Bottle']}
#customer_product_history = {'Ravi': ['Laptop', 'Mouse', 'Keyboard'], 'Anita': ['T-Shirt', 'Jeans', 'Headphones'], 'Sita': ['Mixer', 'Bedsheet'], 'Kiran': ['Shirt', 'Bottle']}
electronics_products = Product_Mapping_Catagory.get('Electronics', [])
#electronics_products = ['Laptop', 'Mouse', 'Keyboard', 'Headphones']

customers_only_electronics = [
    customer for customer, products in customer_product_history.items()
    if all(product in electronics_products for product in products)
]
print("Requirement4: Customers who bought only Electronics:", customers_only_electronics)
print()

# Sorted the customers by their total spending to find the top 3 highest spenders.
#customer_total_spent = {'Ravi': 57300, 'Anita': 5700, 'Sita': 4800, 'Kiran': 2000}
#customer_total_spent.items() = [('Ravi', 57300), ('Anita', 5700), ('Sita', 4800), ('Kiran', 2000)]
#item=('Ravi', 57300)
#item1 = 57300
sorted_customers_by_spending = sorted(customer_total_spent.items(), key=lambda item: item[1], reverse=True)
top_3_highest_spenders = sorted_customers_by_spending[0:3]
print("Requirement4: Top 3 Highest Spenders:", top_3_highest_spenders)
print()

#Requirements5:
#Print a summary of each customer’s total spending and their classification
#Use set operations to find customers who purchased from multiple categories
#Identify common customers who bought both electronics and clothing
"""
customer_product_history = {
    'Ravi':  ['Laptop', 'Mouse', 'Keyboard'],   # all Electronics
    'Anita': ['T-Shirt', 'Jeans', 'Headphones'],# Clothing + Electronics
    'Sita':  ['Mixer', 'Bedsheet'],              # all Home Essentials
    'Kiran': ['Shirt', 'Bottle']                 # Clothing + Home Essentials
}

Product_Mapping_Catagory = {
    'Electronics':     ['Laptop', 'Mouse', 'Keyboard', 'Headphones'],
    'Clothing':        ['T-Shirt', 'Jeans', 'Shirt'],
    'Home Essentials': ['Mixer', 'Bedsheet', 'Bottle']
}
"""
customer_categories = {}       # will store: customer → set of categories
electronics_buyers  = set()    # will store: customers who bought Electronics
clothing_buyers     = set()    # will store: customers who bought Clothing

for customer, products in customer_product_history.items():
    customer_categories[customer] = set()          # empty category set per customer

    for product in products:                        # check each product
        for category, items in Product_Mapping_Catagory.items():
            if product in items:                    # find which category this product belongs to
                customer_categories[customer].add(category)

                if category == 'Electronics':       # while we are here, track Electronics buyers
                    electronics_buyers.add(customer)

                if category == 'Clothing':          # and track Clothing buyers too
                    clothing_buyers.add(customer)

# ── Requirement 5.1 — Summary of spending and classification ───────────

print("=" * 55)
print("  CUSTOMER SPENDING SUMMARY & CLASSIFICATION")
print("=" * 55)

for customer, total_spent in customer_total_spent.items():
    if total_spent >= 6000:
        classification = "High Value Customer"
    elif 5000 <= total_spent < 6000:
        classification = "Moderate Buyer"
    else:
        classification = "Low Value Customer"

    print(f"  {customer:<10}  Spent: ₹{total_spent:<8}  Segment: {classification}")

print()

# ── Requirement 5.2 — Customers from multiple categories ───────────────

multi_category_customers = {
    customer for customer, categories in customer_categories.items()
    if len(categories) > 1
}

print("=" * 55)
print("  CUSTOMERS WHO SHOPPED FROM MULTIPLE CATEGORIES")
print("=" * 55)

for customer in multi_category_customers:
    cats = ", ".join(customer_categories[customer])
    print(f"  {customer} → {cats}")

print()

# ── Requirement 5.3 — Common buyers of Electronics AND Clothing ─────────

common_customers = electronics_buyers & clothing_buyers

print("=" * 55)
print("  BOUGHT BOTH ELECTRONICS & CLOTHING")
print("=" * 55)

if common_customers:
    for customer in common_customers:
        print(f"  {customer}")
else:
    print("  No common customers found.")
