# sly_example.py
from sly import Lexer, Parser

class CalcLexer(Lexer):
    tokens = { NUM, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN }
    ignore = ' \t'

    PLUS    = r'\+'
    MINUS   = r'-'
    MUL     = r'\*'
    DIV     = r'/'
    LPAREN  = r'\('
    RPAREN  = r'\)'
    NUM     = r'\d+'

    def NUM(self, t):
        t.value = int(t.value)
        return t

class CalcParser(Parser):
    tokens = CalcLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', MUL, DIV),
    )

    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr MUL expr',
       'expr DIV expr')
    def expr(self, p):
        if p[1] == '+': return p[0] + p[2]
        elif p[1] == '-': return p[0] - p[2]
        elif p[1] == '*': return p[0] * p[2]
        elif p[1] == '/': return p[0] / p[2]

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUM')
    def expr(self, p):
        return p.NUM

lexer = CalcLexer()
parser = CalcParser()
print(parser.parse(lexer.tokenize("3 + 2 * (5 - 1)")))
