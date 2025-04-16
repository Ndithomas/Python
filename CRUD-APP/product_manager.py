import product as product_mod
import database as db_mod

class ProductManager:
    def __init__(self, auth_manager):
        self.auth_manager = auth_manager
        self.db = db_mod.Database()
        self.product = product_mod.Product(auth_manager.current_user_id) if auth_manager.current_user_id else None
    
    def refresh_product_instance(self):
        if self.auth_manager.current_user_id:
            self.product = product_mod.Product(self.auth_manager.current_user_id)
    
    def handle_create_product(self):
        self.refresh_product_instance()
        print("\nCREATE NEW PRODUCT")
        code = input("Product Code: ")
        name = input("Product Name: ")
        manufacturer = input("Manufacturer: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
        expiry_date = input("Expiry Date (YYYY-MM-DD): ")
        manufacturing_date = input("Manufacturing Date (YYYY-MM-DD): ")
        size = input("Size: ")
        color = input("Color: ")
        
        if self.product.create_product(
            code, name, manufacturer, quantity, price,
            expiry_date, manufacturing_date, size, color
        ):
            print("Product created successfully!")
        else:
            print("Failed to create product")
    
    def handle_search_products(self):
        self.refresh_product_instance()
        print("\nSEARCH PRODUCTS")
        search_term = input("Enter search term (leave blank for all products): ")
        products = self.product.search_products(search_term)
        self.display_products(products)
    
    def handle_update_product(self):
        self.refresh_product_instance()
        print("\nUPDATE PRODUCT")
        product_id = input("Enter product ID to update: ")
        product = self.product.get_product_by_id(product_id)
    
        if not product:
            print("Product not found or you don't have permission")
            return
    
        self.display_products([product])
    
        print("\nEnter new values (leave blank to keep current):")
        updates = {}
        
        fields = [
            ('name', 'Product Name', 3),
            ('manufacturer', 'Manufacturer', 4),
            ('quantity', 'Quantity', 5),
            ('price', 'Price', 6),
            ('expiry_date', 'Expiry Date (YYYY-MM-DD)', 7),
            ('manufacturing_date', 'Manufacturing Date (YYYY-MM-DD)', 8),
            ('size', 'Size', 9),
            ('color', 'Color', 10)
        ]
    
        for field, prompt, index in fields:
            new_value = input(f"{prompt} (current: {product[index]}): ")
            if new_value:
                updates[field] = new_value
    
        if updates:
            if self.product.update_product(product_id, **updates):
                print("Product updated successfully!")
            else:
                print("Failed to update product")
        else:
            print("No changes made")
    
    def handle_delete_product(self):
        self.refresh_product_instance()
        print("\nDELETE PRODUCT")
        product_id = input("Enter product ID to delete: ")
        product = self.product.get_product_by_id(product_id)
        
        if not product:
            print("Product not found or you don't have permission")
            return
        
        self.display_products([product])
        
        confirm = input("Are you sure you want to delete this product? (y/n): ").lower()
        if confirm == 'y':
            if self.product.delete_product(product_id):
                print("Product deleted successfully!")
            else:
                print("Failed to delete product")
    
    def handle_view_all_products(self):
        self.refresh_product_instance()
        print("\nALL PRODUCTS")
        products = self.product.search_products()
        self.display_products(products)
    
    def display_products(self, products):
        if not products:
            print("No products found")
            return
        
        print("\n{:<5} {:<10} {:<20} {:<15} {:<8} {:<10} {:<12} {:<12} {:<10} {:<10}".format(
            "ID", "Code", "Name", "Manufacturer", "Qty", "Price", "Expiry", "Mfg Date", "Size", "Color"
        ))
        print("-" * 120)
        
        for product in products:
            print("{:<5} {:<10} {:<20} {:<15} {:<8} {:<10.2f} {:<12} {:<12} {:<10} {:<10}".format(
                product[0], product[2], product[3], product[4] or '-', product[5], float(product[6]),
                str(product[7] or '-'), str(product[8] or '-'), product[9] or '-', product[10] or '-'
            ))
