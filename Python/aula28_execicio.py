"""
Exercício
peça para o usuário ára digitar seu nome
peça para o usuário ára digitar sua idade
Se nome e idade forem digitado :
    Exiba
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if (nome and idade):
    print('Seu nome é: ',nome)
    print('Seu nome invertido é: ',nome[::-1])

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print('Seu nome tem',len(nome),'letras')
    print('a primeira letra do seu nome é: ',nome[0])
    print('a ultima letra do seu nome é: ',nome[-1])
else:
    print('Desculpe, você deixou campos vazios.')
    