"""
Iterando strings com while
"""
#       012345678910
nome = 'luiz Otávio' #interaveis
#     - 1110987654321

indice = 0 # foi adicionado um indice para contagem
novo_nome = '' # toda variável que entrar precisa ser declarada
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1 # importante lembrar da soma, sem gera o loop

novo_nome += '*'
print(novo_nome)