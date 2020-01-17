import html
from xml.sax.saxutils import unescape

s = 'Elements are written as "<tag>text</tag>".'
print('s', s)
print(html.escape(s))
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'
print(html.unescape(s))


print(unescape('The prompt is &gt;&gt;&gt;'))

