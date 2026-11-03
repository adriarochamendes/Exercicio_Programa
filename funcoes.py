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
def posiciona_frota(frota):
    tabuleiro = []

    for linha in range(10):
        tabuleiro.append([0] * 10)

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro

#QUESTÃO 5
#QUESTÃO 6
#QUESTÃO 7
#QUESTÃO 8
#QUESTÃO 9