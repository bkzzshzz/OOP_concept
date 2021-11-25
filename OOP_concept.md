## Object Oriented Programming Concept in python for beginners

### This is the what a basic class definition in python looks like:

```py
class Item():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        pass
```

### The name of the class is `Item` that has the *attributes* like *name*, *price* and *quantity*. The `def __init__(self, name, price, quantity):` and `def calculate_total_price(self):` under class *Item* are technically funtions but since they are under a class, they are called **Methods**.

### The double underscore methods, like - `__init__`, are called magic methods.

### If there need be to give a default value to an attribute in class initialization:
```py
class Item():
    def __init__(self, name, price, quantity=0):
        pass
```