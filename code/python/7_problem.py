"""
Exercise #07

Faça um programa que receba uma string e responda se ela tem alguma vogal, se sim, quais são?
E também diga se ela é uma frase ou não
"""


str_input = input("Type something here: ")

vowels =  []

if 'a' in str_input:
    vowels.append('a')
if 'e' in str_input:
    vowels.append('e')
if 'i' in str_input:
    vowels.append('i')
if 'o' in str_input:
    vowels.append('o')
if 'u' in str_input:
    vowels.append('u')

if len(vowels) > 0:
    print("\nYes, there are a vowels in the input")
    print(f"They are: {vowels}\n")
else:
    print("No there aren't vowels in the input\n")


if ' ' in str_input:
    print("The input is a phrase")
else:
    print("The input is not a phrase")
