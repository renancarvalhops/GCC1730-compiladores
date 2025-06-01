from sly import Lexer

class JogoLexer(Lexer):
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