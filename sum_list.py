def sum_list(data):
    """
    Calcula a soma de todos os elementos em uma lista.

    Este algoritmo opera com complexidade O(n) porque percorre a lista
    uma única vez para somar seus elementos. O tempo de execução cresce
    linearmente com o número de elementos (n) na lista.

    :param data: Uma lista de números.
    :return: A soma dos elementos da lista.
    """
    # Complexidade: O(n)
    total = 0
    for item in data:
        total += item
    return total

# Teste de uso
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = sum_list(my_list)
    print(f"A lista é: {my_list}")
    print(f"A soma dos elementos é: {result}")
