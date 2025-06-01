from sly import Parser
from JogoLexer import JogoLexer

class JogoParser(Parser):
    tokens = JogoLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', MUL, DIV),
    )

    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr MUL expr',
       'expr DIV expr')
    def expr(self, p):
        match(p[1]):
            case '+': 
                return p[0] + p[2]
            case '-': 
                return p[0] - p[2]
            case '*': 
                return p[0] * p[2]
            case '/': 
                return p[0] / p[2]

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUM')
    def expr(self, p):
        return p.NUM