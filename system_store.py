class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, amount):
        self.quantity += amount
        print(f"{amount} units of {self.name} added, New quantity: {self.quantity}")

    def sell(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            print(f"{amount} units of {self.name} sold, New quantity: {self.quantity}")
        else:
            print(f"Not enough stock of {self.name}. Only {self.quantity} units available.")

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price} EGP, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print(f"Product {product.name} already exists, Use restock method to add more.")
        else:
            self.products[product.product_id] = product
            print(f"Product {product.name} added to inventory.")

    def remove_product(self, product_id):
        if product_id in self.products:
            removed_product = self.products.pop(product_id)
            print(f"Product {removed_product.name} removed from inventory.")
        else:
            print(f"Product with ID {product_id} not found in inventory.")

    def get_product(self, product_id):
        return self.products.get(product_id, None)

    def list_products(self):
        if self.products:
            for product in self.products.values():
                print(product)
        else:
            print("Inventory is empty.")

if __name__ == "__main__":
    product1 = Product(1, "Laptop", 50000, 10)
    product2 = Product(2, "Smartphone", 38500, 25)
    product3 = Product(3, "Headphones", 500, 50)
    product4 = Product(4, "Airbods", 200, 100)
    product5 = Product(5, "Smartwatch", 4000, 45)
    product6 = Product(6, "Ipad", 35000, 37)
    product7 = Product(7, "Mobile Charger", 50, 23)
    product8 = Product(8, "Computer", 4850000, 74)

    inventory = Inventory()

    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)
    inventory.add_product(product4)
    inventory.add_product(product5)
    inventory.add_product(product6)
    inventory.add_product(product7)
    inventory.add_product(product8)

    print("\nCurrent Inventory:")
    inventory.list_products()

    print("\nRestocking product:")
    product1.restock(5)
    product5.restock(9)
    product6.restock(2)

    print("\nSelling product:")
    product2.sell(3)
    product4.sell(7)

    print("\nUpdated Inventory:")
    inventory.list_products()

    print("\nRemoving product:")
    inventory.remove_product(3)
    inventory.remove_product(8)

    print("\nFinal Inventory:")
    inventory.list_products()