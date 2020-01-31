from collections import MutableSequence, Sequence, Iterable, Container, Sized, Mapping
import bisect


class SortedItem(Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItem([5, 3, 1, 4])
print(list(items), items)
items.add(2)
print(*items)

items2 = SortedItem()
print(isinstance(items2, Iterable))
print(isinstance(items2, Container))
print(isinstance(items2, Sized))
print(isinstance(items2, Mapping))

print('-' * 70)


class Items(MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, index):
        print('Getting', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting', index)
        del self._items[index]

    def insert(self, index, value):
        print('inserting', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('len..')
        return len(self._items)


a = Items([1, 2, 3, 7, 5, 4, 6])
print(a, len(a), a.append(3))
print(a.count(3))
a.remove(7)
print(*a)