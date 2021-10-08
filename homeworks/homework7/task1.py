"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0

    for key, value in tree.items():

        # key is str/int/bool case
        counter += 1 if key == element and isinstance(key, type(element)) else 0
        # key is tuple case
        counter += key.count(element) if isinstance(key, tuple) else 0

        # value is str/int/bool case
        counter += 1 if value == element and isinstance(value, type(element)) else 0
        # value is dict case
        counter += find_occurrences(value, element) if isinstance(value, dict) else 0
        # value is set case
        counter += find_occurrences(dict.fromkeys(value), element) if isinstance(value, set) else 0

        # value is list/tuple case
        if isinstance(value, (list, tuple)):
            for item in value:
                # item is str/int/bool case
                counter += 1 if item == element and isinstance(item, type(element)) else 0
                # item is dict case
                counter += find_occurrences(item, element) if isinstance(item, dict) else 0
                # item is set case
                counter += find_occurrences(dict.fromkeys(item), element) if isinstance(item, set) else 0
    return counter
