# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicacao(a,b,c,d,e,f,g):
        multi = a*b*c*d*e*f*g
        return (multi)

print(int(multiplicacao(1,2,3,4,5,6,7)))

#crie uma função que fala se um número é par ou ímpar.
# retorne se o número é par ou ímpar

def resultado(x):
    x = int(x)
    if x % 2 == 0:
        return print('O numero é par!')
    return print (f'o número {x} é ímpar!')

x = input('Digite o número: ')
resultado(x)

"""
Resolução do Professor Luiz Otavio
"""
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicação = multiplicar(10, 2, 3, 4, 5)
print(multiplicação)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)