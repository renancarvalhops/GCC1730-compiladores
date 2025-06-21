from sly import Lexer

class JogoLexer(Lexer):
    tokens = { 'pc', 'pb', 'pe', 'pd', 'repita', 'sair', 'numero' }
    ignore = ' \t\n'

    literals = {'[', ']'}

    pc = r'pc'
    pb = r'pb'
    pe = r'pe'
    pd = r'pd'
    repita = r'repita'
    sair = r'sair'

    @_(r'\d+')
    def numero(self, t):
        t.value = int(t.value)
        return t