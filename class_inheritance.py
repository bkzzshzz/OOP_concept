import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount #class attribute
    all = []
    def __init__(self, name: str, price: float, quantity=0): #method
        
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to Zero!"
        assert quantity >= 0, f"Quantiy {quantity} is not greater than or equal to Zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)


    def calculate_total_price(self): #methods
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}'({self.name})', {self.price}, {self.quantity}"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
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

class Phone(Item): # inheritance
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0): #method
        # Call to super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero"

        # Assign to self object
        self.broken_phones = broken_phones


    def calculate_total_price(self): #methods
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

phone1 = Phone("jscPhonev10", 500, 5, 1)
phone2 = Item("jscPhonec20", 500, 5)

print(Item.all)
print(Phone.all)