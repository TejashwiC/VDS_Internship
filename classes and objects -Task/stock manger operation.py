class Product:
    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"ID: {self.pid}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")
class StockManager:
    def __init__(self):
        self.products = {}

    def add_product(self):
        pid = int(input("Enter Product ID: "))
        if pid in self.products:
            print("Product ID already exists!")
            return
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))
        self.products[pid] = Product(pid, name, price, quantity)
        print(f"Product '{name}' added.")
    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("\nAll Products in Stock:")
            for product in self.products.values():
                product.display()
    def update_stock(self):
        pid = int(input("Enter Product ID to update: "))
        if pid in self.products:
            qty_change = int(input("Enter quantity change (+ to add, - to reduce): "))
            self.products[pid].quantity += qty_change
            print(f"Stock updated. New Quantity = {self.products[pid].quantity}")
        else:
            print("Product not found.")

    def search_product(self):
        pid = int(input("Enter Product ID to search: "))
        if pid in self.products:
            print("Product found:")
            self.products[pid].display()
        else:
            print("Product not found.")

    def remove_product(self):
        pid = int(input("Enter Product ID to remove: "))
        if pid in self.products:
            removed = self.products.pop(pid)
            print(f"Product '{removed.name}' removed.")
        else:
            print("Product not found.")
def main():
    manager = StockManager()
    while True:
        print("\nSTOCK MANAGER MENU")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Remove Product")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            manager.add_product()
        elif choice == "2":
            manager.view_products()
        elif choice == "3":
            manager.update_stock()
        elif choice == "4":
            manager.search_product()
        elif choice == "5":
            manager.remove_product()
        elif choice == "6":
            print("Exiting Stock Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
