"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

print(25*'-')
name = input('Digite seu nome: ')
age = input('Digite sua Idade: ')

if name and age:
    print(f'Seu nome é: {name}')
    print(f'Seu nome invertido é: {name[::-1]}')

    if ' ' in name: #verificando espaço no nome
        print('seu nome contém espaços')
    else:
        print('seu nome não contém espaços')

    print(f'Seu nome {len(name)}')

    print(f'A primeira letra do seu nome é:  {name[0]}')
    print(f'A última letra do seu nome é:  {name[-1]}')
    print(30*'--')

else:
    print("DESCULPE, VOCÊ DEIXOU CAMPOS VAZIOS")

