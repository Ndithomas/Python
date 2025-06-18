import database as db_mod
from datetime import datetime

class Product:
    def __init__(self, user_id):
        self.db = db_mod.Database()
        self.user_id = user_id
    
    def create_product(self, code, name, manufacturer, quantity, price, 
                      expiry_date, manufacturing_date, size, color):
        query = """
        INSERT INTO products 
        (user_id, code, name, manufacturer, quantity, price, 
         expiry_date, manufacturing_date, size, color)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            self.user_id, code, name, manufacturer, quantity, price,
            expiry_date, manufacturing_date, size, color
        )
        
        return self.db.execute_query(query, params)  # No fetch needed for INSERT
    
    def search_products(self, search_term=None):
        query = "SELECT * FROM products WHERE user_id = %s"
        params = (self.user_id,)

        if search_term:
            query += " AND (name LIKE %s OR code LIKE %s OR manufacturer LIKE %s)"
            params += (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%")

        results = self.db.execute_query(query, params, fetch=True)  # Ensure fetch=True
        return results if results else []
    
    def update_product(self, product_id, **kwargs):
        if not kwargs:
            return False
            
        set_clause = ", ".join([f"{k} = %s" for k in kwargs])
        query = f"""
        UPDATE products 
        SET {set_clause}
        WHERE product_id = %s AND user_id = %s
        """
        params = tuple(kwargs.values()) + (product_id, self.user_id)
        
        return self.db.execute_query(query, params)  # No fetch needed for UPDATE
    
    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE product_id = %s AND user_id = %s"
        params = (product_id, self.user_id)
        
        return self.db.execute_query(query, params)  # No fetch needed for DELETE
    
    def get_product_by_id(self, product_id):
        query = "SELECT * FROM products WHERE product_id = %s AND user_id = %s"
        params = (product_id, self.user_id)
        
        result = self.db.execute_query(query, params, fetch=True)  # Use fetch=True for SELECT
        return result[0] if result else None
