class FlatIterator:

    def __init__(self, list_of_list):
        self.flat = []
        self.flat_list(list_of_list)

    # функция-рекурсия для получения "плоского" списка
    def flat_list(self, list_of_elements):
        for el in list_of_elements:
            if isinstance(el, list):
                self.flat_list(el)
            else:
                self.flat.append(el)


    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        # выбрасываем по одному элементу из полученного "плоского" списка
        self.cursor += 1
        if len(self.flat) == self.cursor:
            raise StopIteration
        return self.flat[self.cursor]


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e',
                                                   'f', 'h', False, 1, 2, None,
                                                   '!']


if __name__ == '__main__':
    test_3()