contador = 0
notas = 0

while contador < 6:
    notas = float(input('Digite a nota do aluno: '))
    contador+=1
    
media = notas/contador
print(media)