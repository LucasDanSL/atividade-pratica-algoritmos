def multiply_matrices(matrix_a, matrix_b):
    """
    Multiplica duas matrizes.

    Este algoritmo tem complexidade O(n^2) para matrizes quadradas de
    tamanho n x n, pois utiliza três loops aninhados. O loop externo
    itera sobre as linhas da primeira matriz, o segundo sobre as colunas
    da segunda matriz, e o interno calcula o produto escalar das linhas
    e colunas.

    :param matrix_a: A primeira matriz (lista de listas).
    :param matrix_b: A segunda matriz (lista de listas).
    :return: A matriz resultante da multiplicação.
    """
    # Complexidade: O(n^2) - para matrizes quadradas
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a != rows_b:
        raise ValueError("O número de colunas da matriz A deve ser igual ao número de linhas da matriz B.")

    result_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
    
    return result_matrix

# Teste de uso
if __name__ == "__main__":
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    
    print("Matriz A:")
    for row in matrix1:
        print(row)
        
    print("\nMatriz B:")
    for row in matrix2:
        print(row)
        
    result = multiply_matrices(matrix1, matrix2)
    
    print("\nResultado da Multiplicação:")
    for row in result:
        print(row)
