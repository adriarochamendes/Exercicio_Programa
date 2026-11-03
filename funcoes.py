#QUESTÃO 1
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for deslocamento in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + deslocamento, coluna])
        else:
            posicoes.append([linha, coluna + deslocamento])

    return posicoes
