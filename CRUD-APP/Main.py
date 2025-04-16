import auth_manager as auth_mod
import product_manager as product_mod
import menu as menu_mod

class UStockInventory:
    def __init__(self):
        self.auth_manager = auth_mod.AuthManager()
        self.product_manager = product_mod.ProductManager(self.auth_manager)
        self.menu = menu_mod.Menu(self.auth_manager, self.product_manager)
    
    def run(self):
        while True:
            self.menu.show_current_menu()
            choice = input("Choose option: ")
            
            if not self.auth_manager.is_authenticated():
                self.handle_unauthenticated_choices(choice)
            else:
                self.handle_authenticated_choices(choice)
    
    def handle_unauthenticated_choices(self, choice):
        if choice == '1':
            self.auth_manager.handle_register()
        elif choice == '2':
            self.auth_manager.handle_login()
        elif choice == '3':
            print("Goodbye!")
            exit()
        else:
            print("Invalid option")
    
    def handle_authenticated_choices(self, choice):
        if choice == '6':
            self.auth_manager.handle_logout()
        elif choice == '1':
            self.product_manager.handle_create_product()
        elif choice == '2':
            self.product_manager.handle_search_products()
        elif choice == '3':
            self.product_manager.handle_update_product()
        elif choice == '4':
            self.product_manager.handle_delete_product()
        elif choice == '5':
            self.product_manager.handle_view_all_products()
        else:
            print("Invalid option")

app = UStockInventory()
app.run()
