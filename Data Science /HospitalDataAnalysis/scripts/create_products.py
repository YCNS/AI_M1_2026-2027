# TP 3 -- Question 4
from utils.helpers import clean_lines, parse_products
from utils.product import Product

def main():

    products_list = []

    # Read the File Line by Line
    with open("data/raw/data.txt", "r") as file:
        for line in file:            
            products_list.append(line)
        # or products_list = f.readlines()

    products_list = parse_products(clean_lines(products_list))

    products_objects = []

    for tuple in products_list:
        product = Product(tuple[0], tuple[1], tuple[2])
        products_objects.append(product)
        print(product.total_value())


main()


''' 
# 'py -m scripts.create_products' in the terminal on HospitalDataAnalysis folder to run the code

Expected Output:
Laptop: 3000.0
Phone: 2500.0
Tablet: 1400.0
Monitor: 1200.0
Camera: 400.0
'''
