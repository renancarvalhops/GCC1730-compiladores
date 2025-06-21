from sly import Parser
from JogoLexer import JogoLexer

class JogoParser(Parser):
    tokens = JogoLexer.tokens

    @_('comando')
    def entrada(self, p):
        return p.comando.strip()

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
    
    def error(self, p):
        exemplo_sintaxe = "Alguns exemplos de sintaxes válidas: pd 5 || pd 2 pc 3 || repita 5 [pc 2 pd 3] || pb 1 repita 2 [pe 2 pb 50] || sair"

        if p:
            raise Exception(f"Erro de sintaxe antes do token '{p.value}' na posição {p.index}\n{exemplo_sintaxe}")
        else:
            raise Exception(f"Erro de sintaxe: final inesperado da entrada\n{exemplo_sintaxe}")