# Faça um programa para uma loja de tintas.
#
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada
# Considere que a cobertura da tinta é de 1L para cada 3 metros quadrados e que a
# tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário as quantidades de latas de tinta que necessitam ser compradas
# e o preço total.

# ~> 1L for 3m²
# ~> Each tin contains 18L - costs R$ 80

area = input('What is the size of the area to be painted (m²)? ')

area = int(area)
liters = area / 3

tins_needed = max(1, liters / 18)

if isinstance(tins_needed, float):
    tins_needed = int(tins_needed) + 1

price = tins_needed * 80

print(f'You will need of {liters} ink liters')
print(f'It will cost R$ {price}')
