'''
Formatação básica de strings
s - String
d - int
f - float
.<número de digitos>f
x ou x - hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = 'ABC'
print(f'{variavel}')
# não pode por espaço no final
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.232345325786:0>+10,.1f}')
print(f'{1000.232345325786:0=+10,.1f}')
print(f'O hexadecimal de 1500 é{1500:008x}')
print(f'O hexadecimal de 1500 é{1500:008X}')
print(f'{variavel!r}')