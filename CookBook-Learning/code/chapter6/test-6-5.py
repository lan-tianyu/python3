from xml.etree.ElementTree import Element, tostring
from xml.sax.saxutils import escape, unescape


def dict_to_xml(tag, d):
    elem = Element(tag)
    for k, v in d.items():
        child = Element(k)
        child.text = str(v)
        elem.append(child)
    return elem


s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)
print(e, tostring(e))

e.set('_id', '1234')
print(e, tostring(e))


def dict_to_xml_str(tag, d):
    parts = ['<{}>'.format(tag)]
    for k, v in d.items():
        parts.append('<{0}>{1}</{0}>'.format(k, v))
    parts.append('<{}>'.format(tag))
    return ''.join(parts)


ee = dict_to_xml_str('stcok2', s)
print(ee)

d = {'name': '<spam>'}
a = escape('<sapm>')
print(a)
print(unescape(a))
e = dict_to_xml('test', d)
# print(tostring(e), unescape(tostring(e)))