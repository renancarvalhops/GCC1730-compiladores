from sly import Lexer

class JogoLexer(Lexer):
    tokens = { DIRECAO, SAIR, NUMERO }
    ignore = ' \t'

    DIRECAO = r'pc|pb|pe|pd'
    SAIR = r'sair'

    #Se quiser garantir que STEPS só ocorra depois de uma direção, isso será tratado no parser, não no lexer.
    @_(r'\d+') # type: ignore
    def NUMERO(self, t):
        t.value = int(t.value)
        return t