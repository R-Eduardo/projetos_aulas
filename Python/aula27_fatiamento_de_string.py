"""
Fatiamento de strings
 012345678
 olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs: a fubção len retorna a qtd
de caracteres da str
""" 
vairavel = 'Olá Mundo'
print(vairavel[3:5])
print(len(vairavel[3:5])) #conta caractere
print(vairavel[0:9:2]) #Pulando caractere
print(vairavel[::-2]) #Pulando caractere invertido
print(vairavel[-1:-9:-2]) #Pulando caractere invertido