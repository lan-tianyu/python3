# import mymodule

# a = mymodule.A()
# b = mymodule.B()

# from mymodule.a import A
# from mymodule.b import B

from mymodule import A, B

a = A()
b = B()

print(vars(a), vars(b), a, b)

a.spam()
b.bar()
b.spam()

# class A:
#     def spam(self):
#         print('A...spam')

# class B(A):
#     def bar(self):
#         print('B...bar')
