from database import Database
from product import Product

class ProductManager:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.connect()
        self._initialize_db()
        
    def _initialize_db(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            code VARCHAR(50) UNIQUE NOT NULL,
            name VARCHAR(100) NOT NULL,
            manufacturer VARCHAR(100),
            quantity INT NOT NULL DEFAULT 0,
            price DECIMAL(10,2) NOT NULL,
            expiry_date DATE,
            manufacturing_date DATE,
            size VARCHAR(50),
            color VARCHAR(50)
        )
        """)
        self.conn.commit()
        cursor.close()

    def create_product(self, product):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
            INSERT INTO products 
            (code, name, manufacturer, quantity, price, 
             expiry_date, manufacturing_date, size, color)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                product.code, product.name, product.manufacturer,
                product.quantity, product.price, product.expiry_date,
                product.manufacturing_date, product.size, product.color
            ))
            self.conn.commit()
            product.product_id = cursor.lastrowid
            return product
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"Create failed: {str(e)}")
        finally:
            cursor.close()

    def get_product(self, product_id):
        cursor = self.conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
            result = cursor.fetchone()
            return Product(**result) if result else None
        finally:
            cursor.close()

    def get_all_products(self):
        cursor = self.conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM products")
            return [Product(**row) for row in cursor.fetchall()]
        finally:
            cursor.close()

    def update_product(self, product):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
            UPDATE products SET 
                code = %s, name = %s, manufacturer = %s,
                quantity = %s, price = %s, expiry_date = %s,
                manufacturing_date = %s, size = %s, color = %s
            WHERE product_id = %s
            """, (
                product.code, product.name, product.manufacturer,
                product.quantity, product.price, product.expiry_date,
                product.manufacturing_date, product.size, product.color,
                product.product_id
            ))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"Update failed: {str(e)}")
        finally:
            cursor.close()

    def delete_product(self, product_id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            self.conn.rollback()
            raise Exception(f"Delete failed: {str(e)}")
        finally:
            cursor.close()

    def search_products(self, keyword):
        cursor = self.conn.cursor(dictionary=True)
        try:
            search_term = f"%{keyword}%"
            cursor.execute("""
            SELECT * FROM products 
            WHERE name LIKE %s OR code LIKE %s OR manufacturer LIKE %s
            """, (search_term, search_term, search_term))
            return [Product(**row) for row in cursor.fetchall()]
        finally:
            cursor.close()

    def close(self):
        self.db.close()
