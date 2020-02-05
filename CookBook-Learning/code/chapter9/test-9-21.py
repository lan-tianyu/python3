from functools import partial


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expect value: {} be a str').format(value)
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError('Expect age: {} be int'.format(age))
        self._age = age


# def typed_property(name, expected_type):
#     storage_name = '_' + name

#     @property
#     def prop(self):
#         print('getting..')
#         return getattr(self, storage_name)

#     @prop.setter
#     def prop(self, value):
#         print('value', value, 'expected_type', expected_type)
#         if not isinstance(value, expected_type):
#             raise TypeError('value: {} must be {}'.format(
#                 value, expected_type))
#         setattr(self, storage_name, name)


def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)


class Person1:
    name = typed_property('name', str)
    age = typed_property('age', str)

    def __init__(self, name, age):
        self.name = name
        self.age = age


a = Person('aaaa', 45)
b = Person1('bbbb', 89)
print(a, b, vars(a), vars(b))
a.name = 'ahhh'
a.age = 67

b.age = 'bsfdgd'
b.name = 167

print(vars(a), vars(b))

print('-' * 70)

# String = partial(typed_property, expected_type=str)
# Integer = partial(typed_property, expected_type=int)

String = partial(typed_property, expected_type=str)
Integer = partial(typed_property, expected_type=int)


class Person2:

    name = String('name')
    age = Integer('age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # name = String('name')
    # age = Integer('age')

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age


c = Person2('c', 78)
print(vars(c))
c.name = 'chhh'
c.age = 8
print(vars(c))
c.name = 3243
c.age = 'fsgd'
print(vars(c))
print(c.age, c.name)