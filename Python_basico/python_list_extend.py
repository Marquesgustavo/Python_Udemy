lista_a = [1,2,3,4,5]
lista_b = [10,20,30,40,50]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) #metodo extend, extende a lista, porém não retorna nenhum valor.
print(lista_a)