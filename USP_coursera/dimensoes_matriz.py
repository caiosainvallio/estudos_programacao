def dimensoes_matriz(matriz):
    """
    função que recebe uma matriz como parâmetro e imprime
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

    return (str(linhas) + 'X' + str(colunas))
