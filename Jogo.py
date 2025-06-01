from colorama import Fore
from labirintos import labirintos
from time import sleep
import re

class Jogo:
    def __init__(self, nome):
        self.labirinto = labirintos[nome]

        for i, linha in enumerate(self.labirinto):
            for j, char in enumerate(linha):
                if char == 'J':
                    self.pos_jogador = (i, j)


    def exibir_labirinto(self):
        labirinto = ''

        for linha in self.labirinto:
            for char in linha:
                match(char):
                    case '.':
                        labirinto += '⬛'
                    case '#':
                        labirinto += '🌳'
                    case 'J':
                        labirinto += '🦊'
                    case 'F':
                        labirinto += '🍎'
            labirinto += '\n'

        print(labirinto)


    def pode_mover(self, prox_pos):
        if 0 <= prox_pos[0] < len(self.labirinto) and 0 <= prox_pos[1] < len(self.labirinto[0]):
            return self.labirinto[prox_pos[0]][prox_pos[1]] != '#'
        return False
    

    def mover(self, prox_pos):
        prox_simbolo = self.labirinto[prox_pos[0]][prox_pos[1]]
        self.labirinto[self.pos_jogador[0]][self.pos_jogador[1]] = '.'
        self.pos_jogador = prox_pos
        self.labirinto[self.pos_jogador[0]][self.pos_jogador[1]] = 'J'

        return prox_simbolo == 'F'


    def executar_comando(self, comandos):
        for comando in re.split(r'\s+', comandos):
            if comando == 'q':
                print(Fore.MAGENTA + "Você saiu do jogo.")
                return False
            
            acoes = {
                'w': (-1, 0),
                'a': (0, -1),
                's': (1, 0),
                'd': (0, 1)
            }

            x, y = acoes[comando]
            prox_pos = (self.pos_jogador[0] + x, self.pos_jogador[1] + y)

            if self.pode_mover(prox_pos):
                chegou_final = self.mover(prox_pos)
                self.exibir_labirinto()

                if chegou_final:
                    print(Fore.GREEN + "\nParabéns! Você conseguiu! ✨")
                    return False
            sleep(1)
                
        return True
