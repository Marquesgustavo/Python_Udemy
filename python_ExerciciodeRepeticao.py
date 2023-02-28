""" 
Interando String com o Python
"""
name = 'Lugano'
contador = 0
novo_nome= ''

while contador < len(name):
    letra = name[contador]
    novo_nome += f'*{letra}'
    print(letra)
    print('-'*10)
    print(novo_nome)
    contador += 1

novo_nome += '*'

print('Acabou')