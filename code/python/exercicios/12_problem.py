"""
Exercise #12

Faça um programa que receba uma string, com um número de ponto flutuante, e imprima
qual a parte dele que não é inteira.
"""

number = input('Type a float number:  ')
int_part, dot, float_part = number.partition(".")


print(f'The float part: {float_part}')
