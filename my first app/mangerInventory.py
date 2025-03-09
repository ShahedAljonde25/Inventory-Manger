
import json
import os






def read_inventory():
    with open('inventory.json', 'r') as file:
        data = json.load(file)
    return [Products(product['name'], product['price']) for product in data]

def write_products(products):
    data = [
        {
            'name': product.name,
            'price': product.price
        } for product in products
    ]
    with open('inventory.json', 'w') as file:
        # write the data to the file
        json.dump(data, file)


class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price


  

class MangerInventory:
    def __init__(self):
        self.products = read_inventory()

    def add_product(self):
        name = input("Enter product name: ")
        while True:
            try:
                price = float(input("Enter product price: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid price.")

        new_product = Products(name, price)
        self.products.append(new_product)
        write_products(self.products)


        print("Product added successfully.")

    def view_products(self):
        if self.products:
            print("Product Inventory:")
            for product in self.products:
                print(f"Name: {product['name']}, Price: {product['price']}")
                self.view_products()
        else:
            print("No products in inventory.")

    def update_product(self):
        name = input("Enter the name of the product to update: ")
        for product in self.products:
            if product['name'] == name:
                new_name = input("Enter new product name: ")
                while True:
                    try:
                        new_price = float(input("Enter new product price: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid price.")
                product['name'] = new_name
                product['price'] = new_price

                print("Product updated successfully.")
                return
        print("Product not found.")

    def delete_product(self):
        name = input("Enter the name of the product to delete: ")
        for product in self.products:
            if product['name'] == name:
                self.products.remove(product)
                print("Product removed successfully.")

                return
        print("Product not found.")


def main():
    inventory_system = MangerInventory()

    while True:
        print("""
        1- Add new product
        2- Update product
        3- Show products
        4- Delete product
        5- Exit
        """)
        choice = input("Enter your choice: ")
        if choice in {"1", "2", "3", "4", "5"}:
            if choice == "1":
                inventory_system.add_product()
            elif choice == "2":
                inventory_system.update_product()
            elif choice == "3":
                inventory_system.view_products()
            elif choice == "4":
                inventory_system.delete_product()
            elif choice == "5":
                break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()