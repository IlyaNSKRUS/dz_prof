class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_of_list_cursor = 0
        self.nested_of_list_cursor = 0
        return self

    def __next__(self):
        if self.list_of_list_cursor == (len(self.list_of_list) - 1) and self.nested_of_list_cursor == len(self.list_of_list):
            raise StopIteration
        else:

            len_nested_list = len(self.list_of_list[self.list_of_list_cursor])
            if self.nested_of_list_cursor < len_nested_list:
                item = (self.list_of_list[self.list_of_list_cursor][self.nested_of_list_cursor])
                self.nested_of_list_cursor += 1
            else:
                self.list_of_list_cursor += 1
                self.nested_of_list_cursor = 0
                item = (self.list_of_list[self.list_of_list_cursor][self.nested_of_list_cursor])
                self.nested_of_list_cursor += 1
        return item

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
