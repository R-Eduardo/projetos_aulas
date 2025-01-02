# nome = input('qual o seu nome')
# print(f'O seu nome é {nome}')

#forma que pode errar
#numero_1= int(input('Digite um número: '))
#numero_2= int(input('Digite outro número: '))

#forma correta
numero_1= ('Digite um número: ')
numero_2= ('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2= int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2 }')