# Inheritance

### As the name suggests it is about inheriting one's charactersitcs/attributes/methods from one class to another. The class from which attributes/methods are inherited is called the `Parent class` and one which is inheriting is called `Child class`.

### Inheritance is done from a single line like: 
```py
class Phone(Item):
    pass
```

### A simple inheritance
```py
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
```

### `super().__init__()` here takes all the self objects from the parent class such that we don't have to assign to self objects here.

```py
def __repr__(self):
    return f"{self.__class__.__name__}'({self.name})', {self.price}, {self.quantity}"
```

### In the magic method `__repr__` we use `self.__class__.__name__` to know either the instance is called from the parent class or the child class. 

### For example:
```py
phone1 = Phone("jscPhonev10", 500, 5, 1)
phone2 = Item("jscPhonec20", 500, 5)

print(Item.all)
print(Phone.all)
```
### The output will be:
```
[Phone'(jscPhonev10)', 500, 5, Item'(jscPhonec20)', 500, 5]
[Phone'(jscPhonev10)', 500, 5, Item'(jscPhonec20)', 500, 5]
```

