"""
Operadores lógicos
and (e) or (ou) not (não)
and - todas as condições precisam ser
verdadeiras.
se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor
são consideradas falsy (que vc já viu)
0 0.0 '' False
Também existe o tipo None que é
usado para apresentar um não valor

"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

#if condição True
if entrada == 'E'and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curco circuito
print(True and False and True)
print(True and 0 and True)

#Retornaram falsy
print(bool(0))
print(bool(0.0))
print('')