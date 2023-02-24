"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá Mundo'
print(10*'-')
print(variavel[0:5])
print(10*'-')
print(len(variavel)) #contagem de caracteres
print(variavel[0:9:2]) #fatiando a variavel com passo de 2.