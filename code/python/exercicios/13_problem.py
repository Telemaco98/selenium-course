"""
Exercise #13

Faça um programa que, dada uma lista [1, 2, 3, 4, 5, 6, 7, 8, 7, 10] e um número
inteiro, imprima a tabuada desse número
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = int(input('Please, type an integer number:  '))

print(f" {5 * '*'} The Multiplication Table of {x} {5 * '*'}")

for n in numbers:
    print(f"{x} x {n} = {x * n}")
