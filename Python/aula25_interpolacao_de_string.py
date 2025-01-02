'''
Interpolação básica de strings
s - string
d e i int
f - float
x e x Hexadecimal (ABCDEF0123456789)
'''
nome = "luiz"
preco = 1000.95897643
#variavel = '%s, o preço é R$' % nome
variavel = '%s, o preço é R$%.2f' % (nome,preco)
print(variavel)

#hexadecimal
print('O hexadecimal de %d é %04X' % (15,15))
#a quantidade de place holder precisa ser igual
#colocando o 'x' maiusculo transorma todos em maiusculo


