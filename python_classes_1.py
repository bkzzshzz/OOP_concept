class Item:
    def __init__(self, name: str, price: float, quantity=0): #method
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to Zero!"
        assert quantity >= 0, f"Quantiy {quantity} is not greater than or equal to Zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self): #methods
        return self.price * self.quantity


item1 = Item("Laptop", 100, 5)
# print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item("Mobile", 10, 20)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

# item2.has_numpad = False

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))
# print(item2.calculate_total_price(item2.price, item2.quantity))

# print(item1.name, item1.price, item1.quantity)
# print(item2.name, item2.price, item2.quantity)