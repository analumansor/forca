## coding: utf-8

## Jogo da Forca
## Exercício de Programação Orientada a Objetos

# Importanto pacote
import random

tabuleiro = ['''
>>>>>>>>>>>>>>> FORCA <<<<<<<<<<<<<<<
 +---+
 |   |
     |
     |
     |
     |
 =========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
==========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
==========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Criacao da Classe
class Forca:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_certas = []

        # Metodo para adivinhar a letra
    def guess (self, letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

        # Metodo para verificar se o jogo terminou
    def forca_over(self):
        return self.forca_won() or (len(self.letras_erradas) == 6)

        # Metodo para verificar se o jogador venceu
    def forca_won(self):
        if '_' not in self.hide_word():
            return True
        return False

        # Metodo para esconder a palavra no tabuleiro
    def hide_word(self):
        rtn = ''
        for letter in self.palavra:
            if letter not in self.letras_certas:
                rtn += '_'
            else:
                rtn += letter
        return rtn

        # Metodo para checar o status do game e imprimir o tabuleiro na tela
    def print_game_status(self):
        print(tabuleiro[len(self.letras_erradas)])
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas: ',)
        for letra in self. letras_erradas:
            print(letra,)
        print()
        print('Letras corretas: ',)
        for letra in self.letras_certas:
            print(letra)
        print()

# Funcao para escolher uma palavra aleatoriamente no banco de palavras
def random_word():
    with open("Palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

# Metodo Main - Execução do programa
def main():
    # Objeto
    game = Forca(random_word())

    # Enquanto o jogo nao tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.forca_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_game_status()

   # De acorco com o status, imprime mensagem na tela para o usuário
    if game.forca_won():
        print('\n Parabens! Voce venceu :)')
    else:
       print('Fim de jogo! Voce perdeu :(')
       print('A palavra era:' + game.palavra)

# Execução do programa
if __name__ == '__main__':
    main()