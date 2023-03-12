"""
Exercício
Exiba os índices da lista
    Exemplo:
    0 Maria
    1 Helena
    2 Luiz

"""

lista = ['Maria', 'Helena', 'Luiz']
i = 0
i_negativo = -1

for nome in lista:
    print(f'{i} - {nome}')
    print(f'{i_negativo} - {nome}')
    i += 1
    i_negativo -= 1

# resolução do professor Otavio:
    """
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))