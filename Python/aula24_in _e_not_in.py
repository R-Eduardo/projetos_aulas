"""
Operadores in e not in
Strings são interáveis
0  1 2 3 4 5
O  t a v i o
-6-5-4-3-2-1
"""

nome = 'Otávio'
print(nome[2])
print(nome[-4])

print('á' in nome)
print('z' in nome)
print(10  * '-')
print('á' not in nome)
print('z' not in nome)

#game
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print (f'{encontrar}não esta em {nome}')

