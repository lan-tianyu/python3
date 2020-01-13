data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(data, len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

print('-' * 50)

x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

x = 523**23
print(x.bit_length())
nbytes, rem = divmod(x.bit_length(), 8)
nbytes += 1 if rem else 0
print(nbytes, rem)
print(x.to_bytes(nbytes, 'big'))
print(x.to_bytes(nbytes, 'little'))