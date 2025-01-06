""" While/else """

string = 'Valor qualquer'

i = 0 # condição do indice precisa ser colocado 

while i < len(string):
    letra = string [1]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
    
print ('fora do while.') # esse argumento já esta fora da estrutura while