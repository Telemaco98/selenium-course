"""
Exercise #09

Faça um programa que peça uma nota entre zero e 10. Mostre uma mensagem caso o
valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

grade = -1

while grade < 0 or grade > 10:
    grade = int(input("Insert a value between 0 and 10:  "))
else:
    print(f"""The grade is {grade}

        {'*' * 5} THE END {'*' * 5}
    """)
