"""
Exercise #06

Faça um programa que pergunte o preço de três produtos e informe qual produto você
deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

print("Type the product prices:\n")
price_01 = float(input("Price #01: "))
price_02 = float(input("Price #02: "))
price_03 = float(input("Price #03: "))

if price_01 <= price_02 and price_01 <= price_03:
    print(f'\nYou should buy the product #1 with price {price_01}')
elif price_02 <= price_01 and price_02 <= price_03:
    print(f'\nYou should buy the product #2 with price {price_02}')
else:
    print(f'\nYou should buy the product #3 with price {price_03}')
