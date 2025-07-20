class FlatIterator:

    def __init__(self, list_of_list):
        self.list = []
        # распаковываем входящий список в "плоский"
        for list1 in list_of_list:
            for element in list1:
                self.list.append(element)

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.list) == self.cursor:
            raise StopIteration
        return self.list[self.cursor]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()