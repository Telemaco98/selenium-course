"""
Exercise #08

Faça um programa que receba uma data de nascimento (15/07/87) e imprima

'Você nasceu em <dia> de <mês> de <ano>'
"""

birth_date = input("Type your birth date: ")

birth_date_list = birth_date.split('/')
day = birth_date_list[0]
month = birth_date_list[1]
year = birth_date_list[2]

# other way to do it:
# day, month, year = birth_date.split('/')

print(f'Você nasceu em {day} de {month} de {year}')
