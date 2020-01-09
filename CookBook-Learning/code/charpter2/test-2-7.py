import re

text1 = 'Computer says "no."'
str_pat = re.compile(r'"(.*)"')
print(str_pat.findall(text1))

text2 = text1 = 'Computer says "no.", Phone says "yes."'
print(str_pat.findall(text2))

str_pat1 = re.compile(r'"(.*\.)",')
print(str_pat1.findall(text2))

str_pat2 = re.compile(r'"(.*?)"')
print(str_pat2.findall(text2))