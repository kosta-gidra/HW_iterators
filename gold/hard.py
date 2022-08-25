# второй способ для ниндзя итераторов

my_list_hard = [
    [],
    [1, [2], 3, 4, [5, 6, 7]],
    [8, 9, 10, 11],
    [12, 13, 14, [[[[15]]]]], []
]


class FlatIteratorV2:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.iterators_stack = [iter(self.multi_list)]  # стэк итераторов
        return self

    def __next__(self):
        while self.iterators_stack:  # пока в стеке есть итераторы
            try:
                current_element = next(self.iterators_stack[-1])
                #  пытаемся получить следующий элемент
            except StopIteration:
                self.iterators_stack.pop()
                continue
            if isinstance(current_element, list):
                # если следующий элемент оказался списком, то
                # добавляем его итератор в стек
                self.iterators_stack.append(iter(current_element))
            else:
                # если элемент не список, то просто возвращаем его
                return current_element
        raise StopIteration

def flat_generator_v2(multi_list):
    for item in multi_list:
        if isinstance(item, list):
            # если элемент списка оказывается списком то оборачиваем в этот же генератор
            # такой прием называется рекурсия
            for sub_item in flat_generator_v2(item):
                yield sub_item
        else:
            yield item

if __name__ == '__main__':
    print('Задача 3')
    for item in FlatIteratorV2(my_list_hard):
        print(item)
    print('*' * 25)

    print('Задача 4')
    for item in flat_generator_v2(my_list_hard):
        print(item)
    print('*' * 25)