"""
Exercise #21

Dada uma lista de entradas de usuários de numeros inteiros, construa um dicionário
com a lista padrão, a lista de valores elevados ao quadrado e a lista dos valores
elevados ao cubo.
"""

def func_21 (lista = [0, 1, 3, 5, 12, 32]):
    set_result = {}
    set_result["default_list"] = lista

    quadrado_list = []
    for l in lista:
        quadrado_list.append(l ** 2)
    set_result["quadrado_list"] = quadrado_list

    cubo_list = []
    for l in lista:
        cubo_list.append(l ** 3)
    set_result["cubo_list"] = cubo_list

    return set_result
