from xml.etree.ElementTree import iterparse
from xml.etree.ElementTree import parse
from collections import Counter
import os


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError as e:
                print('Error: ', e)


dir_path = os.path.abspath(os.path.join(os.path.abspath(__file__),
                                        '../../../'))
file_name = os.path.join(dir_path, 'tmp/somefile2.xml')

potholes_by_zip = Counter()
doc = parse(file_name)
print('doc...', doc)
for pothole in doc.iterfind('row/row'):
    potholes_by_zip[pothole.findtext('zip')] += 1
for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)


data = iterparse(file_name, ('start', 'end'))
print(next(data))