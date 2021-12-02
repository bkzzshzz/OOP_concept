# Getters and Setters

### Before starting with getters and setters, the files are divided into groups such that the parent class and the child class are a separate files in their own respect.

### With `from item import Item` in *phone.py* file the properties of the class *Item* is imported from *item.py* file. And in *main.py* we `from item import Item` again to access both the files from one main file.

### Read-only attributes

### `@property` as a decorator sets read-only attributes.
```py
@property
def read_only_name(self):
    return "AAA"
```

```py
from item import Item

item1 = Item("MyItem", 750)

# Setting an attribute
item1.name = "OtherItem"

# Getting an attribute
print(item1.name)
```

```py
@property
# Property decorator = Read-Only Attribute
def name(self):
    return self.__name

@name.setter
def name(self, value):
    self.__name = value
```

### The use of double-underscores(dunders) is a convention when using getters and setters.

### For setter, there need to be a second argument like: 
```py
@name.setter 
    def name(self, value):
```
> `value` is the second argument.
