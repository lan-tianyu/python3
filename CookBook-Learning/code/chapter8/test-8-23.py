import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    @property
    def parent(self):
        print(self, 'get parent...')
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        print(self, 'set parent..')
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


root = Node('parent')
c1 = Node('child1')
c2 = Node('child2')
root.add_child(c1)
root.add_child(c2)
print(c2.parent)
del root
print(c2.parent)

print('-' * 70)


class Data:
    def __del__(self):
        print('Data delete...')


class Node1:
    def __init__(self):
        self.data = Data()
        self._parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child._parent = self

    @property
    def parent(self):
        return 'Node({!r:})'.format(self.data)

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)


a = Data()
del a
a = Node1()
del a
print('-' * 70)
a = Node1()
a.add_child(Node1())
del a

print('-' * 50)

a = Node1()
a_ref = weakref.ref(a)
print(a_ref())
print('-' * 50)

del a
print('-' * 50)

print(a_ref())