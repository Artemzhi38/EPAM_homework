

"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from typing import Iterator


def file_gen(file):
    with open(file) as current_file:
        for line in current_file:
            yield int(line)


class OneFromEach:
    def __init__(self, file_list):
        self.file_list = file_list
        self.values = ["None" for file in file_list]
        self.generators = []
        for file in self.file_list:
            self.generators.append(file_gen(file))

    def refresh_values(self):
        for pos, value in enumerate(self.values):
            if value == "None":
                self.values[pos] = next(self.generators[pos], "None")

    def __iter__(self):
        return OneFromEachIter(self)


class OneFromEachIter:
    def __init__(self, one_from_each: OneFromEach):
        one_from_each.refresh_values()
        self.one_from_each = one_from_each
        self.values = one_from_each.values

    def __iter__(self):
        return self

    def __next__(self):
        self.one_from_each.refresh_values()
        if self.values.count("None") < len(self.values):
            int_values = []
            for value in self.values:
                if isinstance(value, int):
                    int_values.append(value)
            result = min(int_values)
            self.one_from_each.values[
                self.one_from_each.values.index(result)
            ] = "None"
            return result
        raise StopIteration


def merge_sorted_files(file_list) -> Iterator:
    return iter([value for value in OneFromEach(file_list)])
