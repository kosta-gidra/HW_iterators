from itertools import chain

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator(list):

    def __iter__(self):
        self.iterator = chain.from_iterable(self[:])
        return self

    def __next__(self):
        next_list = next(self.iterator)
        return next_list


if __name__ == '__main__':
    for i in FlatIterator(nested_list):
        print(i)
    print()
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
