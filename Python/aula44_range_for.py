"""
For + Range
range -. range(start, stop, step)
         range(5 ,10 , 2)
"""
#numeros = range(0, 10, 1) ele não contará o ultimo pois começa em zero
numeros = range(0, -10, -1)

for numero in numeros:
    print(numero)