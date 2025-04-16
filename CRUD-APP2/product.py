class Product:
    def __init__(self, product_id=None, code=None, name=None, manufacturer=None, 
                 quantity=0, price=0.0, expiry_date=None, manufacturing_date=None, 
                 size=None, color=None):
        self.product_id = product_id
        self.code = code
        self.name = name
        self.manufacturer = manufacturer
        self.quantity = quantity
        self.price = price
        self.expiry_date = expiry_date
        self.manufacturing_date = manufacturing_date
        self.size = size
        self.color = color
        
    def to_dict(self):
        return {
            'product_id': self.product_id,
            'code': self.code,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'quantity': self.quantity,
            'price': self.price,
            'expiry_date': self.expiry_date,
            'manufacturing_date': self.manufacturing_date,
            'size': self.size,
            'color': self.color
        }
