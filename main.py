from colorama import Fore, init
from Jogo import Jogo

if __name__ == "__main__":
    init(autoreset=True)

    jogo = Jogo("teste")
    print(Fore.BLUE + "Trabalho de Compiladores 2025.1")
    print("Grupo: Gabriel Franco, Gilmar Santos, Juan Carvalho, e Renan Carvalho\n")
    jogo.exibir_labirinto()

    jogando = True
    while jogando:
        comandos = input(Fore.YELLOW + "\nComandos: ").lower()
        # tokens = lexer.tokenize(comandos)
        # result = parser.parse(tokens)
        jogando = jogo.executar_comando(comandos)
