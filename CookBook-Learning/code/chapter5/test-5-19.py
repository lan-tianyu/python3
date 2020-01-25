from tempfile import TemporaryFile
from tempfile import TemporaryDirectory
from tempfile import NamedTemporaryFile

with TemporaryFile('w+t') as f:
    f.write('Hello world')
    f.write('Testing\n')
    f.seek(0)
    data = f.read()
    print('data:', data)


with NamedTemporaryFile('w+t') as f:
    print('filename:', f.name)

with TemporaryDirectory() as dirname:
    print('dirname:', dirname)


with NamedTemporaryFile('w+t', prefix='mytemp', suffix='.txt', dir='tmp') as f:
    print('filename', f.name)

f.close()
print('filename', f.name)

