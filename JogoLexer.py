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
    
    def error(self, t):
        raise Exception(f"Token inválido: {t.value.split(" ")[0]} --> Tokens válidos: pc pb pe pd repita [ ] sair")