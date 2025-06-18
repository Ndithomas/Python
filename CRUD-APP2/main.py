from product import Product
from product_manager import ProductManager

class Menu:
    def __init__(self, product_manager):
        self.product_manager = product_manager
    
    def show_menu(self):
        while True:
            print("\nPRODUCT MANAGEMENT")
            print("1 - Create Product")
            print("2 - Search Products")
            print("3 - Update Product")
            print("4 - Delete Product")
            print("5 - View All Products")
            print("6 - Exit")

            choice = input("Select an option: ")

            if choice == '1':
                self.create_product()
            elif choice == '2':
                self.search_products()
            elif choice == '3':
                self.update_product()
            elif choice == '4':
                self.delete_product()
            elif choice == '5':
                self.view_all_products()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

    def create_product(self):
        try:
            code = input("Code: ")
            name = input("Name: ")
            manufacturer = input("Manufacturer: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            expiry_date = input("Expiry Date (YYYY-MM-DD): ")
            manufacturing_date = input("Manufacturing Date (YYYY-MM-DD): ")
            size = input("Size: ")
            color = input("Color: ")

            product = Product(
                code=code, name=name, manufacturer=manufacturer,
                quantity=quantity, price=price,
                expiry_date=expiry_date, manufacturing_date=manufacturing_date,
                size=size, color=color
            )
            self.product_manager.create_product(product)
            print("Product created successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def search_products(self):
        keyword = input("Enter keyword to search: ")
        results = self.product_manager.search_products(keyword)
        for p in results:
            print(p.to_dict())

    def update_product(self):
        product_id = int(input("Enter product ID to update: "))
        product = self.product_manager.get_product(product_id)
        if not product:
            print("Product not found.")
            return

        print("Leave blank to keep existing value.")
        product.name = input(f"Name [{product.name}]: ") or product.name
        product.code = input(f"Code [{product.code}]: ") or product.code
        product.manufacturer = input(f"Manufacturer [{product.manufacturer}]: ") or product.manufacturer
        product.quantity = int(input(f"Quantity [{product.quantity}]: ") or product.quantity)
        product.price = float(input(f"Price [{product.price}]: ") or product.price)
        product.expiry_date = input(f"Expiry Date [{product.expiry_date}]: ") or product.expiry_date
        product.manufacturing_date = input(f"Manufacturing Date [{product.manufacturing_date}]: ") or product.manufacturing_date
        product.size = input(f"Size [{product.size}]: ") or product.size
        product.color = input(f"Color [{product.color}]: ") or product.color

        success = self.product_manager.update_product(product)
        if success:
            print("Product updated.")
        else:
            print("Failed to update product.")

    def delete_product(self):
        product_id = int(input("Enter product ID to delete: "))
        success = self.product_manager.delete_product(product_id)
        print("Deleted successfully." if success else "Failed to delete product.")

    def view_all_products(self):
        products = self.product_manager.get_all_products()
        for p in products:
            print(p.to_dict())


manager = ProductManager()
menu = Menu(manager)
menu.show_menu()
manager.close()
