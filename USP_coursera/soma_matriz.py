def dimensoes_matriz(matriz):
    """
    Função que recebe uma matriz como parâmetro e imprime
    as dimensões da matriz recebida, no formato iXj.

    Exemplos:

    minha_matriz = [[1], [2], [3]]
    dimensoes(minha_matriz)
    3X1

    minha_matriz = [[1, 2, 3], [4, 5, 6]]
    dimensoes(minha_matriz)
    2X3
    """
    linhas = len(matriz)
    colunas = len(matriz[0])

    return f'{linhas}X{colunas}'


def soma_matrizes(m1, m2):
    """
    Função recebe 2 matrizes e devolve uma matriz que represente sua soma caso as
    matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

    Exemplos:

    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    soma_matrizes(m1, m2)
    [[3, 5, 7], [9, 11, 13]]

    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    soma_matrizes(m1, m2) => False
    """
    if dimensoes_matriz(m1) == dimensoes_matriz(m2):
        matriz = []
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                valor = m1[i][j] + m2[i][j]
                linha.append(valor)
            matriz.append(linha)
        return matriz
    else:
        return False


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    print(soma_matrizes(A, B))