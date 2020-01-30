import requests


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        # return self.template.format_map(kwargs)
        return requests.get(self.template.format_map(kwargs)).contant


yahoo = UrlTemplate(
    'http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
# print(line.decode('utf-8'))
print(yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'))
