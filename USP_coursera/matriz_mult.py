def sao_multiplicaveis(m1, m2):
    """
    Função que recebe duas matrizes como parâmetro e devolve True se as
    matrizes forem multiplicavéis (na ordem dada) e False caso contrário.

    * Obs. Duas matrizes são multiplicáveis se o número de
    colunas da primeira é igual ao número de linhas da segunda.

    Exemplos:

    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    sao_multiplicaveis(m1, m2) => False

    m1 = [[1], [2], [3]]
    m2 = [[1, 2, 3]]
    sao_multiplicaveis(m1, m2) => True
    """
    if len(m1[0]) == len(m2):
        r = True
    else:
        r = False
    return r
