"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""
"""
v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))
"""
condicao = False
passou_no_if = True

if condicao:
    passou_no_if = True
    print("faça algo")
else:
    print("não faça algo")

#print(passou_no_if, passou_no_if is None)
#print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')
if passou_no_if is not None:
    print('Passou no if')