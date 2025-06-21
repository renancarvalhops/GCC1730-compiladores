from colorama import Fore, init
from Jogo import Jogo
from JogoLexer import JogoLexer
from JogoParser import JogoParser

if __name__ == "__main__":
    init(autoreset=True)

    jogo = Jogo("facil")
    print(Fore.BLUE + "Trabalho de Compiladores 2025.1")
    print("Grupo: Gabriel Franco, Gilmar Santos, Juan Carvalho, e Renan Carvalho\n")
    lexer = JogoLexer()
    parser = JogoParser()
    jogo.exibir_labirinto()

    jogando = True
    while jogando:
        comandos = input(Fore.YELLOW + "\nComandos: ").lower()
        tokens = lexer.tokenize(comandos)
        resultado = parser.parse(tokens)
        print(resultado)
        jogando = jogo.executar_comando(resultado)
