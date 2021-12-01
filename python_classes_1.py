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
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# item1 = Item("Laptop", 100, 5)
# print(item1.calculate_total_price(item1.price, item1.quantity))

# item2 = Item("Mobile", 10, 20)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)
# print(Item.__dict__)
# print(item1.__dict__)
# item2.has_numpad = False

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))
# print(item2.calculate_total_price(item2.price, item2.quantity))

# print(item1.name, item1.price, item1.quantity)
# print(item2.name, item2.price, item2.quantity)



item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
# for instance in Item.all:
#     print(instance.name)


