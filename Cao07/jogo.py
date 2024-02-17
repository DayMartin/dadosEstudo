import random
from os import system, name

# Função para limpeza da tela ao iniciar o jogo
def limpar():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Linux e Mac
    else: 
        _ = system('clear')

def game():
    limpar()
    
    print('Bem vindo a este jogo')
    print('As palavras que você deve adivinhar são da categoria "Fruta"')
    print('Vamos começar!')
    print('OBS: O número de chances é baseado no tamanho da palavra que você precisa adivinhar')

    #Lista de palavras
    palavras = ['Banana', 'Goiaba', 'Uva', 'Morango', 'Abacate', 'Abacaxi']

    #Escolher as palavras aleatoriamente
    palavra = random.choice(palavras).lower()

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # # numero de chances baseado no valor da palavra
    numero_de_chances = len(letras_descobertas)

    # Numero de chances
    chances = numero_de_chances

    #Armazenar as letras erradas
    erradas = []

    while chances > 0:

        #Print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:",chances)
        print('Letras erradas:', " ".join(erradas))

        #Tentativa
        tentativa = input('\nDigite uma letra: ').lower()

        #Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            erradas.append(tentativa)


        # Verificar se o usuario ganhou ou perdeu
            
        if "_" not in letras_descobertas:
            print('Parabéns você adivinhou, a palavra é:', palavra)
            break

    if "_" in letras_descobertas:
        print('Você perdeu todas as chances, a palavra era:', palavra)


if __name__ == '__main__':
    game()