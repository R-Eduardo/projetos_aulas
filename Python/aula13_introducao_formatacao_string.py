nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = (peso / (altura * altura))

#f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pessa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

#Luiz ortávio tem 1.80 de allura,
#pessa 95 quilos e seu IMC é
#29.320987654320987

print(linha_1)
print(linha_2)
print(linha_3)