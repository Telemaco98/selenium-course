"""
Faça um program que peça dois números inteiros e um número float. Calcule e mostre

1. O produto do dobro do primeiro com a metade do segundo.
2. A soma do triplo do primeiro com o terceiro
3. O terceiro elevado ao cubo
"""

num_01 = int(input("Type an int number: "))
num_02 = int(input("Type other int number: "))
num_03 = float(input("Type a float number: "))

result_01 = (2 * num_01) * (num_02 / 2)
result_02 = 3 * num_02 + num_03
result_03 = num_03 ** 3

print("\n\n__Results__")
print(f'Result 01: {result_01}')
print(f'Result 02: {result_02}')
print(f'Result 03: {result_03}')
