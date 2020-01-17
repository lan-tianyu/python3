text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.rjust(20, '='))
print(text.ljust(20, '-'))

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))

print(format(text, '=>20'))
print(format(text, '*^20'))

print('{:>10s}{:>10s}'.format('hello', 'world'))

print(format(1.25, '=>20'))

print(format(1.25, '^10.2f'))