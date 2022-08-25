# первый способ для ниндзя итераторов

my_list_simple = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]


class FlatIterator:

    def __init__(self, multi_list):

        self.multi_list = multi_list  # список с воложенными списками

    def __iter__(self):
        self.multi_list_iter = iter(self.multi_list)
        self.nested_list = []  # вложенный список с элементами
        self.nested_list_cursor = -1
        return self

    def __next__(self):
        self.nested_list_cursor += 1
        if len(self.nested_list) == self.nested_list_cursor:
            self.nested_list = None
            self.nested_list_cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.multi_list_iter)
                #  если  список пустой, то получаем следующий
                #  если списки закончаться, получим stop iteration

        return self.nested_list[self.nested_list_cursor]


class FlatIteratorEasyWay:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        return chain.from_iterable(self.multi_list)


def flat_generator(my_list):
    for sub_list in my_list:
        for item in sub_list:
            yield item

if __name__ == '__main__':
    print('Задача 1')
    for item in FlatIterator(my_list_simple):
        print(item)
    print('*' * 25)
    print('Задача 2')
    for item in flat_generator(my_list_simple):
        print(item)
    print('*' * 25)