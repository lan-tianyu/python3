import re

text1 = '/* this is a comment */'
text2 = '''/* this is \n multiline comment */ \n'''

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text1))
print(comment.findall(text2))

comment1 = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment1.findall(text1))
print(comment1.findall(text2))
