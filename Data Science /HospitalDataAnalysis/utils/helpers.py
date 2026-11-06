# TP 3 -- Question 1
def clean_lines(list_string):

    cleaned_list = [s.strip() for s in list_string if s.strip()]
    return cleaned_list

'''
lines = ["Laptop,1000,3", " ", "Phone,500,5", "\n", "Tablet,700,2"]
clean_lines(lines)
print(clean_lines(lines))

# Expected Output:
# ["Laptop,1000,3", "Phone,500,5", "Tablet,700,2"]
'''


# TP 3 -- Question 2
def  parse_products(lines):
    products = []
    for line in lines:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) != 3:
            continue
        name, price, quantity = parts
        if not name:
            continue
        try:
            products.append((name, float(price), int(quantity)))
        except ValueError:
            continue
    return products

'''
lines = ["Laptop,1000,3", "Phone,500,5", "Tablet,700,2"]
print(parse_products(lines))

# Expected Output:
# [("Laptop", 1000.0, 3), ("Phone", 500.0, 5), ("Tablet", 700.0, 2)]
'''
