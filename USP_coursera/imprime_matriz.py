def imprime_matriz(mat):
    """
    Função que recebe uma matriz como parâmetro e imprime a matriz, linha por linha.
    """
    for i in range(len(mat)):
        cont = 0
        for j in range(len(mat[i])):
            if cont < len(mat[i])-1:
                print(mat[i][j], end=' ')
            else:
                print(mat[i][j], end='')
            cont += 1
        print()
