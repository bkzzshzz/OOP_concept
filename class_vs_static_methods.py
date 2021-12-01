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




#     def __repr__(self):
#         return f"Item('{self.name}', {self.price}, {self.quantity})"

# Item.instantiate_from_csv()
# print(Item.all)

print(Item.is_integer(7.0))




