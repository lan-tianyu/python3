import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))


def matchcase(word):
    def replace(m):
        print('m:', m)
        text = m.group()
        if text.isupper():
            return word.upper()
        if text.islower():
            return word.lower()
        if text[0].isupper():
            return word.capitalize()
    return replace


print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))


