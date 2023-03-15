"""
Valores padrão para parâmetros
Ao definir uma funçãço, os parâmetros podem 
ter valores padrão. Caso o valor nãoç seja
enviado para o parâmetro, o valor ádrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x,y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} resultado= ', x + y + z)
    else:
        print(f'{x=} {y=} resultado= ', x + y)

soma(1,2)
soma(10,70)
soma(550, 880)