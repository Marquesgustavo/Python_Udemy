"""
Faça uma lista de compras
O usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programas quebre com erros
de índices inexistentes na lista
"""
lista = ['Maça', 'Manga', 'Mamão']
entrada = ''
fruta_adionada = ''
fruta_apagada = ''
inserir = 'i'
apagar = 'a'
listar = 'l'

while True: 
    print(lista)
    entrada = input('[i] -  inserir , [a] = apagar e [l] - listar novamente: ')
    x = entrada.lower()

    if inserir == x:
            fruta_adionada = input('Digite a Fruta que deseja adicionar: ')
            lista.append(fruta_adionada)
    elif apagar == x:
           for indice, frutas in enumerate(lista):
                  print(indice, lista[indice])

    else:
        continue
            





