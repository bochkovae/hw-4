import types


def flat_generator(list_of_list):
    flat_list = []
    # делаем список "плоским" при помощи рекурсии
    def recursion(some_list):
        for el in some_list:
            if isinstance(el, list):
                recursion(el)
            else:
                flat_list.append(el)
    recursion(list_of_list)
    # из нового "плоского" списка выбрасываем по одному элементу
    for el in flat_list:
        yield el


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()