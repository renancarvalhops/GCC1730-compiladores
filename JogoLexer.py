from sly import Lexer

class JogoLexer(Lexer):
    tokens = { UP, DOWN, LEFT, RIGHT, STEPS }
    ignore = ' \t'

    UP = r'w'
    DOWN = r's'
    LEFT = r'a'
    RIGHT = r'd'
    #ATTACK
    #JUMP


    #Se quiser garantir que STEPS só ocorra depois de uma direção, isso será tratado no parser, não no lexer.
    @_(r'\d+') # type: ignore
    def STEPS(self, t):
        t.value = int(t.value)
        return t