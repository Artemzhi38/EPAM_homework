"""
Values can be strings or integer numbers. If a value can be
treated both as a number and a string, it is treated as number.

has its keys and values accessible as collection items
and as attributes

In case of attribute clash existing built-in attributes
take precedence.

In case when value cannot be assigned to
an attribute (for example when there's a line 1=something)
ValueError should be raised.
"""
import os.path


path = os.path.join(os.path.dirname(__file__), 'task1.txt')
storage = KeyValueStorage(path)
print(storage.name)
print(storage['name'])
print(storage.power)
print(storage.keys)
print(storage['keys'])
print(storage)
print(storage.__dict__)
print(KeyValueStorage.__dict__)

