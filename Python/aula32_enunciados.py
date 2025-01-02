"""
Faça um programa que peça ao usuário para digitar 
um número inteiro,
informe se este número é par ou impar. Caso o 
usuário não digite um número
inteiro, informe que não é um numero inteiro.

numero = int(input('digitar um número inteiro: '))

par = ((numero % 2) == 0)
impar = ((numero % 2) == 1)

if par :
    print('O numero é par')
elif impar:
    print('O numero é impar')
else:
    print('numero não valido')
"""

"""
entrada = input('Digite um núemro: ')
if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
"""

"""
entrada = input('Digite um núemro: ')
try:
     entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')
"""

"""
Faça um porgrama que pergunte a hora ao usuário e,
 baseando-se no horário
descrito, exiba a saudação apropriada. 
ex: Bom dia 0-11, Boa tarde 12-17, e boa noite 18-23.
"""
"""
hora = int(input('Digite um horário: '))

manha = hora >= 0 and hora <= 11
tarde = hora >= 12 and hora <= 17
noite = hora >= 18 and hora<= 23

if manha:
    print('Bom dia')
elif tarde:
    print('Boa tarde')
elif noite:
    print('Boa noite')
"""
"""
entrada = input("Digite a hora: ")
try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora<= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor apenas digite números inteiros')
"""

"""
Faça um programa que peça o primeiro nome do usu
ário.se o nome tiver 4 letras ou menos
escreva "seu nome é curto"; se tiver entre 5 e 6 letras, 
escreva"seu nome é normal"; maior que 
6 escreva "seu nome é muito grande".
"""



nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >=5 and tamanho_nome <=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')