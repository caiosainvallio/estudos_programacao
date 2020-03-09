def cria_matriz(num_linhas, num_colunas):
    """
    Cria e retorna uma matriz com num_linhas linhas e
    num_colunas colunas em que cada elemento é igual
    valor dado.
    """
    matriz = []
    valor = 0
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            while True:
                try:
                    valor = int(input(f'Digite o elemento [{i}][{j}]: '))
                except ValueError:
                    print('ERRO! Digite um valor válido.')
                    continue
                else:
                    break

            linha.append(valor)
        matriz.append(linha)
    return matriz


def le_matriz():
    """
    Função auxiliar para introduzir elemetos de uma matriz
    na função cria_matriz()
    """
    lin = col = 0
    while True:
        try:
            lin = int(input('Digite o número de linhas: '))
        except ValueError:
            print('ERRO! Digite um valor válido.')
            continue
        else:
            break
    while True:
        try:
            col = int(input('Digite o número de colunas: '))
        except ValueError:
            print('ERRO! Digite um valor válido.')
            continue
        else:
            break
    return cria_matriz(lin, col)


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


def imprime_matriz(mat):
    """
    Função que recebe uma matriz como parâmetro e imprime a matriz, linha por linha.
    """
    print()
    print('-' * 42)
    print(f'{"Resultado da multiplicação de matrizes":^42}')
    print('-' * 42)
    print()
    for i in range(len(mat)):
        cont = 0
        for j in range(len(mat[i])):
            if cont < len(mat[i])-1:
                print(mat[i][j], end=' ')
            else:
                print(mat[i][j], end='')
            cont += 1
        print()
    print()
    print('-' * 42)


def multiplicacao_matriz():
    """
    Função recebe duas matrizes, certifica se são multiplicáveis, se sim,
    faz a multiplicação e por fim imprime na tela.
    """
    m = []
    while True:
        print('Matriz A:')
        m1 = le_matriz()
        print('\nMatriz B:')
        m2 = le_matriz()
        if not sao_multiplicaveis(m1, m2):
            print('Matrizes não multiplicáveis, tente novamente.\n')
            continue
        else:
            for linha in range(len(m1)):
                m.append([])
                for coluna in range(len(m2[0])):
                    m[linha].append(0)
                    for k in range(len(m1[0])):
                        m[linha][coluna] += m1[linha][k] * m2[k][coluna]
            break
    imprime_matriz(m)


if __name__ == '__main__':
    multiplicacao_matriz()
