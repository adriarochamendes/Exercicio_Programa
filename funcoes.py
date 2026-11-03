#QUESTÃO 1
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for deslocamento in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + deslocamento, coluna])
        else:
            posicoes.append([linha, coluna + deslocamento])

    return posicoes

#QUESTÃO 2
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = []

    frota[nome_navio].append(posicoes)

    return frota

#QUESTÃO 3
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"

    return tabuleiro

#QUESTÃO 4
#QUESTÃO 5
#QUESTÃO 6
#QUESTÃO 7
#QUESTÃO 8
#QUESTÃO 9