# Class Methods

### Self vs Cls

> `self` refers to an instance of a class whereas `cls` refers to a class. 

```py
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
```

### `def instantiate_from_csv(cls):` is for class only. 

### `@classmethod` is a decorator used to define a method to instantiate a class from a csv file. CSV stands for comma separated values. 

### The csv file `items.csv` has the contents:
```
name,price,quantity
"Phone",100,1
"Laptop",1000,3
"Cable",10,5
"Mouse",50,5
"Keyboard",75.5,5
```

### `reader = csv.DictReader(f)` converts the file into a dictionary and it is further converted into a list by `items = list(reader)`.

```py
for item in items:
    Item(
        name = item.get('name'),
        price = float(item.get('price')),
        quantity = float(item.get('quantity')),
    )
```
### `name = item.get('name')` gets the item name from the list.



# Static Methods

```py
@staticmethod
def is_integer(num):
    if isinstance(num, float):
        return num.is_integer()
    elif isinstance(num, int):
        return True
    else:
        return False
```

### The decorator `@staticmethod` is used to initiate static methods. `isinstance()` checks if the type of a number belongs to an instance of a given class like: *int*, *float*, etc. 

### When to use class methods and when to use static methods?

```py
class Item:
    @staticmethod
    def is_integer(num):
        '''
        This should do something that has a relationship with the class, but not something that must be unique per instance!
        '''

    @classmethod
    def instantiate_from_something(cls):
        '''
        This should also do something that has a relationship with the class, but usually, those are used to manipulate different structures of data to instantiate objects like we have done with csv.
        '''
```




