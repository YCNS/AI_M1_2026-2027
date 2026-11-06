# TP 3 -- Question 3
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

'''
p = Product("Laptop", 1000, 3)
print(p.total_value()) #  Output: 3000
'''
