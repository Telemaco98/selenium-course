"""
Exercise #11

Faça um programa que itera em uma string e toda vez que uma vogal aparecer na sua string
printa seu nome entre as letras
"""

str = input('Type something here: ')
vowels = "aeiou"

for s in str:
    if s in vowels:
        print('OHARA')
    else:
        print(s)
