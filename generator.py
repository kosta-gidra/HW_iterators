nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(lists):
    for list_ in lists:
        for item in list_:
            yield item


if __name__ == '__main__':
    for i in flat_generator(nested_list):
        print(i)
