class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.len_list_of_lists = len(list_of_list)
        self.counter = -1

    def __iter__(self):
        self.counter += 1
        self.list_counter = 0
        return self

    def __next__(self):
        if self.list_counter == len(self.list_of_list[self.counter]):
            iter(self)
        if self.counter == self.len_list_of_lists:
            raise StopIteration
        self.list_counter += 1
        return self.list_of_list[self.counter][self.list_counter - 1]


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