"""
Retorno de calores das funções (return)
somente as funcoes e metodos tem o "return"
"""

def soma(x,y):
    return x + y #return transforma minha funcao para devolver um valor
            

soma1 = soma(2,2)
soma2 = soma(8,9)
print(soma1 + soma2)

def soma_luizotavio(x, y):
    if x > 10:
        return [10, 20]
    return x + y


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma_luizotavio(2, 2)
soma2 = soma_luizotavio(3, 3)
print(soma1)
print(soma2)
print(soma_luizotavio(11, 55))