from item import Item

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
