"""
Iterável -> str, Range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu interador

"""
"""
texto = 'Luiz'.__iter__()
texto = iter('Luiz') #.__iter__()

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())

(__) esse espaço é chamado de dander
"""
"""
texto = iter('Luiz')
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
"""

"""
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
"""

"""
# for lettra in texto
texto = 'Luiz' # interável
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break        
"""
texto = 'Luiz' # interável
for letra in texto:
    print(letra)
