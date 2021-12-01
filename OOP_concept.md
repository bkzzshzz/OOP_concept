## Object Oriented Programming Concept in python for beginners

### Link to the video: https://www.youtube.com/watch?v=Ej_02ICOIgs&list=PLYkeTZVGTsUiKwM2JoI472PWZMAHAZrQL&index=4&t=1877s

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

### Class Attribute

```py
class Item:
    pay_rate = 0.8
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        pass
item1 = Item("Laptop", 10, 20)
item2 = Item("Mobile", 10, 20)

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)
print(Item.__dict__)
print(item1.__dict__)
```
### The `pay_rate` is a class attribute. Here, `item1` and `item2` are instances of class `Item`. But, `pay_rate` is the only the attribute of class `Item`. But, since they are the instances of `Item` they can access the class attrbute and print the value or `pay_rate`. `__dict__` is a magic attribute that shows the attributes that a class and its instances hold.  


> We can see that the attrbutes held by the instance `item1` are `{'name`: 'Laptop', 'price':100, 'quantity': 5}`

### The `Item.pay_rate` accesses the value from the class. Hence, cannot be altered if not altered in the class.
```py
def apply_discount(self):
    self.price = self.price * Item.pay_rate
item1.pay_rate = 0.8
```

### But here, it can be altered.
```py
def apply_discount(self):
    self.price = self.price * self.pay_rate
item1.pay_rate = 0.8
```

### About `all` attribute: The `all` attribute or a list, is a list that stores the information of all the instances of a class. Very helpful.

```py
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
```

### First we create an empty list called `all` and append all the instances to the list by `Item.all.append(self)`. To access the contents of `all`:

```py
print(Item.all)
for instance in Item.all:
    print(instance.name)
```

### `print(Item.all)` shows the memory address of all the instances and the for loop is to access the names of each instance.

### Another magic method `__repr__`. This helps in representing data of an instance. Like:

```py
def __repr__(self):
    return f"Item('{self.name}', {self.price}, {self.quantity})"
```

### Pass the instances with `def __repr__(self):` and print all with formatted string.