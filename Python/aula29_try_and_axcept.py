"""
Introdução ao try/except
try -> tenta executar o código
except -> ocorreu algum erro ai tentar executar
"""

"""
print(123)
print(456)
int('a') #ValueError: invalid literal for int() with base 10: 'a'
"""


numero_str = input('Vou dobrar o numero que digitar: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso nãoé um número')


if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Isso nãoé um número')


