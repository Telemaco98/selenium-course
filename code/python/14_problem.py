"""
Exercise #14

Faça um programa que dada a entrada de uma lista o programa faz o cálculo
acumulativo da mesma

Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saída: [1, 3, 6, 10]
"""

input_ = []
exit = ""
while exit != "exit":
    try:
        exit = int(input("Type an integer number:  "))
        input_.append(exit)
    except:
        exit = "exit"


output = []
sum = 0

for i in input_:
    sum = sum + i
    output.append(sum)

print(f"\n\n\tResulted list: {output}")
