import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount #class attribute
    all = []
    def __init__(self, name: str, price: float, quantity=0): #method
        
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to Zero!"
        assert quantity >= 0, f"Quantiy {quantity} is not greater than or equal to Zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
    
    
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        print("You are trying to get.")
        return self.__name

    @name.setter
    def name(self, value):
        print("You are trying to set.")
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value
    
    def calculate_total_price(self): #methods
        return self.__price * self.quantity
    

    @classmethod
    def instantiate_from_csv(cls):
        with open('/home/bikesh/Desktop/python/OOP_concept/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity')),
            )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    
    def __repr__(self):
        return f"{self.__class__.__name__}'({self.name})', {self.__price}, {self.quantity}"
