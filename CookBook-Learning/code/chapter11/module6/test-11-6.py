from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:15000', allow_none=True)
s.set('foo', 'bar')
s.set('spam', [1, 2, 3, 4])
print(s, s.get('spam'), s.exists('foo'), s.key())
s.delete('foo')
print(s, s.key())

# def add(x, y):
#     print(x + y)

# serv = SimpleXMLRPCServer(('', 8080))
# serv.register_function(add)
# serv.serve_forever()