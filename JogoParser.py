from sly import Parser
from JogoLexer import JogoLexer

class JogoParser(Parser):
    tokens = JogoLexer.tokens

    @_('comando')
    def entrada(self, p):
        return p.comando

    @_('acao comando')
    def comando(self, p):
        return " ".join([p.acao, p.comando])

    @_('estrutura comando')
    def comando(self, p):
        return " ".join([p.estrutura, p.comando])

    @_('')
    def comando(self, p):
        return ''

    @_('direcao numero')
    def acao(self, p):
        return " ".join(p.direcao * p.numero)

    @_('sair')
    def acao(self, p):
        return 'q'

    @_('repita numero "[" comando "]"')
    def estrutura(self, p):
        return "".join(p.comando * p.numero)

    @_('pc')
    def direcao(self, p):
        return 'w'

    @_('pb')
    def direcao(self, p):
        return 's'

    @_('pe')
    def direcao(self, p):
        return 'a'

    @_('pd')
    def direcao(self, p):
        return 'd'