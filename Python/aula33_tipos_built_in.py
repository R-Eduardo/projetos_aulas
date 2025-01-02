"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos str, int, float, bool
"""

# # Tentativa de fazer mudança no código em valor imultável
# string = "luiz Otávio"
# # outra_variavel = sring
# string[3] = 'ABC'
# print(string[3])

#Só daria para mudar se criar outra vairável
string = "luiz Otávio"
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)