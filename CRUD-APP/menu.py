class Menu:
    def __init__(self, auth_manager, product_manager):
        self.auth_manager = auth_manager
        self.product_manager = product_manager
    
    def show_current_menu(self):
        if not self.auth_manager.is_authenticated():
            self.show_unauthenticated_menu()
        else:
            self.show_authenticated_menu()
    
    def show_unauthenticated_menu(self):
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
    
    def show_authenticated_menu(self):
        print("\nPRODUCT MANAGEMENT")
        print("1 - Create Product")
        print("2 - Search Products")
        print("3 - Update Product")
        print("4 - Delete Product")
        print("5 - View All Products")
        print("6 - Logout")