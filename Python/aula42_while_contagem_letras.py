frase = 'O Python é uma linguagem de progração' \
    'Multiparadigma' \
    'Python foi criado por Guido van Rossum'

#.upper() letra maiuscula
#.lower() letra minuscula
#.count() Conta a Palavra

#print(frase.count('Python'))


i = 0 
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1 # lembre de mover ou copiar
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1 #interando 

print('A letra apareceu mais vezes foi'
      f'{letra_apareceu_mais_vezes} que apareceu'
      f'""{qtd_apareceu_mais_vezes}" x '
      
      
      )

# linhas = 2
# colunas = 2
 
# linha = 1
# while linha <= linhas:
#     coluna = 1
#     while coluna <= colunas:
#         print(linha, coluna)
#         coluna += 1
#     linha += 1