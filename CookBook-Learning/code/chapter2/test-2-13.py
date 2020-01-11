text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.rjust(20, '='))
print(text.ljust(20, '-'))

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
