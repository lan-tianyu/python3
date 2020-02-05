import dis
import opcode


def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op > opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i + 1] * 256 + extended_arg
            extended_arg = 0
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue
        else:
            oparg = None

        yield (op, oparg)


def add(x, y):
    return x + y


c = add.__code__
print(c, c.co_code)


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('end...')


print(countdown.__code__.co_code)
print('-' * 70)


for op, oparg in generate_opcodes(countdown.__code__.co_code):
    print(op, opcode.opname[op], oparg)

print('-' * 70)
# print(dis.dis(countdown))

c = countdown.__code__.co_code

print(opcode.opname[c[0]], opcode.opname[c[1]], opcode.opname[c[2]])
