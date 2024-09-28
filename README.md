# Inventory-management-system
Object of the project :
Creating a simple inventory management system for an electronics company that helps track the products available in the store and their price, which enables the products to be managed effectively by implementing some operations such as adding products, restocking products, the selling process, updating the warehouse, and the process of removing unwanted or unavailable products.

Class product:

Represent a products in the inventory.

Contains some Method:

1- __init__ :Initializes the product,it contains some Attributes:
Product_id : The product ID.
Name: The name of product.
Price : The price of product.
Quantity : The quantity of the product in the stock.

2- restock : Adds a certain amount of the product , by collection the amount to the old quantity in the inventory .

3- Sell : Sells a certain amount of the product , If the quantity in the inventory is greater than the amount, the amount is subtracted from the quantity in the inventory  , if the amount is larger the output is not enough stock.

4- __str__ : Display product details.

Class inventory:

Manages a collection of products.

Contains some Method:

1- __init__ : Initializes the inventory , and contain an Attributes products : A dictionary containing products (key : product_id , value : product object).

2- add_product : Adds a product to the inventory.

3- remove_product : Removes a product to the inventory.

4- get_product : Retrieves a product to the inventory. 

5- list_product : Displays all products to the inventory.

if __name__ == "__main__":
It guarantees that the code inside this condition will only be executed when the file is run directly.

product1 = Product() :  
Create products.

inventory = Inventory():
Create inventory.

inventory.add_product(product1)
Add products to inventory.

inventory.list_products()
Display products.

product1.restock(5)
Restock products.

product2.sell(3)  
Sell products.

inventory.remove_product(3)
Remove a products from inventory.


