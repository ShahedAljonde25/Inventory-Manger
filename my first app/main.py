

import json

from Products import Products
def read_inventory():
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            return [Products(product['name'], product['price']) for product in data]
    except FileNotFoundError:
        return []

def write_products(products):
    data = [{'name': product.name, 'price': product.price} for product in products]
    with open('inventory.json', 'w') as file:
        json.dump(data, file)

class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price




class InventoryManager:
    def _init_(self):
        self.products = read_inventory()

    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        new_product = Products(name, price)
        self.products.append(new_product)
        write_products(self.products)
        print("Product added successfully.")

    def view_products(self):
        if self.products:
            print("Product Inventory:")
            for product in self.products:
                print(f"Name: {product.name}, Price: {product.price}")
                write_products(self.products)

        else:
            print("No products in inventory.")

    def update_product(self):
        name = input("Enter the name of the product to update: ")
        for product in self.products:
            if product.name == name:
                new_name = input("Enter new product name: ")
                new_price = float(input("Enter new product price: "))
                product.name = new_name
                product.price = new_price
                print("Product updated successfully.")
                write_products(self.products)

                return
        print("Product not found.")


    def delete_product(self):
        name = input("Enter the name of the product to delete: ")
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print("Product deleted successfully.")

                write_products(self.products)

            return
    print("Product not found.")    



def main():
    inventory_system = InventoryManager
    print("Product Inventory Management")
    while True:
     print("""
     Choose one of the below operations:
         1. Add Product - Add a new product to the inventory.
         2. View Products - Display all products in the inventory.
         3. Update Product - Modify the details of an existing product.
         4. Delete Product - Remove a product from the inventory.
         5. Exit - Exit the application.
        """)
     choice = input("Enter your choice: ")

     if choice == '1':
        inventory_system.add_product()
     elif choice == '2':
        inventory_system.view_products()
     elif choice == '3':
        inventory_system.update_product()
     elif choice == '4':
        inventory_system.delete_product()
     elif choice == '5':
         print("Exiting the application.")
         break
     else:
        print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()