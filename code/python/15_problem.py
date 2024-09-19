"""
Exercise #15

Faça um programa que dada a entrada de uma lista o programa calcule a
combinatória de dois elementos e nos retorne as combinações em uma nova lista

Exemplo de entrada: [1, 2, 3, 4]
Exemplo de saída: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
"""

input_ = []
exit = ""
while exit != "exit":
    try:
        exit = int(input("Type an integer number:  "))
        input_.append(exit)
    except:
        exit = "exit"

print(f"\n\n\tInput: {input_}")
output = []

for i in input_:
    copy_of_input = input_.copy()
    copy_of_input.remove(i)

    for j in copy_of_input:
        new_comb = [i, j]
        output.append(new_comb)
    input_ = copy_of_input

print(f"\n\n\tCombinations: {output}")
