import re
from collections import namedtuple

NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join(
    [NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS]))

TOKEN = namedtuple('Token', ['type', 'value'])


def generator_token(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type is not 'WS':
            yield tok


class ExpressionEvalutor:
    def parse(self, text):
        self.tokens = generator_token(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        return self.expr()

    def _advance(self):
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)
    
    def _accept(self, toktype):
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    def _expect(self, toktype):
        if not self._accept(toktype):
            raise SyntaxError('Exceptions, except toktype: {}'.format(toktype))

    def expr(self):
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            else:
                exprval -= right
        return exprval

    def term(self):
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIED'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUTIMESS':
                termval *= right
            else:
                termval /= right
        return termval

    def factor(self):
        if self._accept('NUM'):
            return int(self.tok.value)
        if self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('PAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')
        
