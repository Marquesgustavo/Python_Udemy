
#Gustavo da Silva
#28 de Fevereiro de 2023
#Exercio de Palavra Secreta do curso de Python dentro da plataforma Udemy
#Prfessor Luiz Otavio Miranda

palavra_secreta = 'Cadeado'

usuario_tentativa = ''
acertos_usuario = ''

for letra in palavra_secreta:
    #print(letra)
    usuario_tentativa = input('Digite sua tentativa, apenas uma letra: ')
    if letra == usuario_tentativa:
        acertos_usuario = acertos_usuario + usuario_tentativa
        print(acertos_usuario)

    else:
        print('*******')
        

    

