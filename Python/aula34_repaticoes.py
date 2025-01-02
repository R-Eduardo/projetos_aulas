"""
Repetições
While (enquanto)
Executa uma ação equanto uma donição for verdadeira.
loop infino quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input ("qual o seu nome: ")
    print(f'Seu nime é {nome}')

    if nome == 'sair':
        break
print('Acabou')