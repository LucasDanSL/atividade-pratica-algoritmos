def power(base, exp):
    """
    Calcula a potência de um número usando exponenciação por quadratura.

    Este algoritmo recursivo tem complexidade O(log n), onde n é o expoente.
    A cada chamada recursiva, o problema é dividido pela metade (exp // 2),
    o que resulta em um crescimento logarítmico do número de operações
    em relação ao expoente.

    :param base: O número base.
    :param exp: O expoente.
    :return: O resultado de base elevado a exp.
    """
    # Complexidade: O(log n)
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    else:
        half = power(base, (exp - 1) // 2)
        return base * half * half

# Teste de uso
if __name__ == "__main__":
    base_num = 2
    exponent = 10
    result = power(base_num, exponent)
    print(f"{base_num} elevado a {exponent} é: {result}")
