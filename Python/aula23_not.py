# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')
#------------------------------------
if senha == '123456':
    print('Entrou')
else:
    print('Senha incorreta.')
#------------------------------------
if senha != '123456':
    print('Entrou')
else:
    print('Senha incorreta.')
#------------------------------------
if not senha:
    print('Senha Incorreta')
else:
    print('Senha incorreta.')
#------------------------------------
print(not True)  #false
print(not False) #true
