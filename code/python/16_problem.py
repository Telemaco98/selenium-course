"""
Exercise #16

Faça um programa, com uma função, que calcula a média de uma lista.
Tip: Funções embutidas que podem te ajustar:
    len(list) -> calcula o tamanho da lista
    sum(list) -> faz o somatório dos valores
"""

def average(list_):
    return sum(list_)/len(list_)

example = [0, 1, 2, 3, 4, 5]        # result 15 / 6 =  2.5
result = average(example)

print(result)
