"""
Exercise #05

Faça um programa para a leitura de duas notas pariciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

 - A mensagem "Aprovado", se a média alcançada for maior ou igual a 7.
 - A mensagem "Reprovado", se a média alcançada for menor do que 7.
 - A mensagem "Aprovado por Distinção", se a média alcançada for menor do que 10.
"""

grade_01 = float(input("Grade #1: "))
grade_02 = float(input("Grade #2: "))

average = (grade_01 + grade_02) / 2

print(f"\nAverage {average}")
print("\n__Results__")

if average == 10:
    print('Aprovado por Distinção')
elif average >= 7:
    print('Aprovado')
else:
    print('Reprovado')
