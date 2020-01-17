import io

s = io.StringIO(initial_value='dsisj', newline='')
print(s.read())

s1 = io.StringIO()
s1.write('fsjkm ')
print(s1.getvalue())


s3 = io.StringIO(initial_value='Hello\nWorld\n', newline='')
print(s3.read(4), s3.read())

ss = io.BytesIO(b'hjkn ')
print(ss.getvalue(), ss.read())