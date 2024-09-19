"""
Exercise #17

Faça um programa, com uma função, que calcula a mediana de uma lista
Tip: Funções embutidas que podem te ajustar:
    sorted(list) -> ordena uma lista
"""

def median(list_):
    list_.sort()
    list_len = len(list_)
    if list_len % 2 == 1:                   # if the lenght is pair
        return list_[list_len // 2]         # return the middle number
    else:                                   # else, it's odd
        sum = list_[(list_len -1) // 2] + list_[list_len // 2]
        return sum / 2                      # return sum of two middle numbers divided by 2


# [0 1 2 3 4] len = 5, result = 2
example_1 = [4, 1, 3, 2, 0]
print(median(example_1))

# [0 1 2 3 4 5] len = 6, result = 2.5
example_2 = [4, 5, 1, 3, 2, 0]
print(median(example_2))
