"""We have a file that works as key-value storage, each line is
represented as key and value separated by = symbol, example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers. If a value can be
treated both as a number and a string, it is treated as number.
Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')

that has its keys and values accessible as collection items
and as attributes. Example:

storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay'
storage.power # will be integer 9001

In case of attribute clash existing built-in attributes
take precedence. In case when value cannot be assigned to
an attribute (for example when there's a line 1=something)
ValueError should be raised. File size is expected to be
small, you are permitted to read it entirely into memory."""

import re


class KeyValueStorage(dict):

    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file
        dictionary = {}
        with open(path_to_file) as file:
            for line in file:
                key, value = line.strip().split("=")
                if not re.match(r"^[a-zA-Z_][\w]*$", key):
                    raise ValueError
                try:
                    value = int(value)
                except ValueError:
                    pass
                dictionary[key] = value
                try:
                    getattr(self, key)
                except AttributeError:
                    self.__dict__[key] = value
        super().__init__(self, **dictionary)
