"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
condicao = True

while condicao:
    name = input('Qual o seu nome:')
    print(f'Seu nome é {name}')

    if name == 'sair':
        break

print('Acabou')

