import textwrap
import os

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print(textwrap.fill(s, 70))
print(textwrap.fill(s, 30))
print(textwrap.fill(s, 30, initial_indent='   '))
print('-' * 50)
print(textwrap.fill(s, 30, subsequent_indent='    '))

print(os.get_terminal_size().columns)
print(textwrap.fill(s, os.get_terminal_size().columns))