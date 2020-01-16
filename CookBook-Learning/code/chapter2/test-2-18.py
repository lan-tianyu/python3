import re
from collections import namedtuple

text = 'foo = 23 + 42 * 10'

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.scanner('foo = 42')
print(scanner.match().lastgroup, scanner.match().group())


def genrate_token(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


print(list(genrate_token(master_pat, text)))
print([tok for tok in genrate_token(master_pat, text) if tok.type != 'WS'])

print('*' * 50)

LT = r'(?P<LT>>)'
LE = r'(?P<LE>>=)'
EQ = r'(?P<EQ>=)'
master_pat1 = re.compile('|'.join([LE, LT, EQ]))
print(list(genrate_token(master_pat1, '=>=>')))


PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
master_pat2 = re.compile('|'.join([PRINT, NAME]))
print(list(genrate_token(master_pat2, 'printers')))