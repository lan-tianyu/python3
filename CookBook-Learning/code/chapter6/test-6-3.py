import os
# import requests
from xml.etree.ElementTree import parse

# u = requests.get('http://planet.python.org/rss20.xml')
# doc = parse(u.content)
# print('doc', doc)

dir_path = os.path.abspath(os.path.join(os.path.abspath(__file__),
                                        '../../../'))
file_name = os.path.join(dir_path, 'tmp/somefile.xml')
doc = parse(file_name)
print('doc\n', doc)
print('-' * 70)

for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print('title: ', title)
    print('date: ', date)
    print('link: ', link)