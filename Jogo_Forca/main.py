import random


def bem_vindo():
    print('BEM VINDO AO JOGO DA FORCA')


def gera_palavra_secreta():
    palavras = ['arroz', 'feijao', 'banana', 'maca', 'elefante', 'mouse', 'mesa', 'celular', 'camisa', 'switch']
    index = random.randint(0, len(palavras) - 1)
    return palavras[index]


def gera_palavra_vazia(qtde_caracteres):
    palavra_vazia = []

    for i in range(qtde_caracteres):
        palavra_vazia.append('_')

    return palavra_vazia


def status(palavra, erros):
    print(palavra)
    print('Erros: ' + str(erros) + '\n')


if __name__ == '__main__':
    bem_vindo()
    palavra_secreta = gera_palavra_secreta()
    palavra_jogo = gera_palavra_vazia(len(palavra_secreta))

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        status(palavra_jogo, erros)
        letra_chute = input("Qual Letra? \n")

        if letra_chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if letra_chute == letra:
                    palavra_jogo[posicao] = letra
                posicao += 1
        else:
            erros += 1

        if erros == 6:
            enforcou = True
            print('Você perdeu --- Enforcado!')

        if '_' not in palavra_jogo:
            acertou = True
            print('Você Ganhou!')
            print(palavra_secreta)
