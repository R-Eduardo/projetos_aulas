"""
Repetições
While (enquanto)
Executa uma ação equanto uma donição for verdadeira.
loop infino quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1
    
    if contador == 6:
        print('Não vou mostar ',contador)
        continue
    
    if contador >= 10 and contador <= 27:
        print('Não vou mostar ',contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')