"""
Exercise #10

Faça um programa que leia 5 números e informe o maior número
"""

count = 1
biggest = int(input('Type a number:  '))

while count < 5:
    current = int(input('Type a number:  '))
    if current > biggest:
        biggest = current
    count += 1
else:
    print(f"The biggest number is: {biggest}")
