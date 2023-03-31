"""
Exercício de perguntas e respostas
"""
resposta_usuario_01 = ''
resposta_usuario_02 = ''
resposta_usuario_03 = ''

def validacao(x,y,z):
    if x == p1.get('Resposta'):
        return True
     
    

p1 = {
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1', '3', '4', '5'],
    'Resposta': '4',
    }
p2 = {
    'Pergunta': 'Quanto é 5*5?',
    'Opções': ['25', '55', '10', '51'],
    'Resposta': '25',
}
p3 = {
    'Pergunta': 'Quanto é 10/2?',
    'Opções': ['4', '5', '2', '1'],
    'Resposta': '5',
}

print('---------Pergunta 01----------')
print(p1.get('Pergunta'))
print(p1.get('Opções'))
resposta_usuario_01 = input('Digite sua resposta: ')

if validacao(resposta_usuario_01) == True:    
    print('Voce acertou')
else:
    print('Resposta errada!')

print('---------Pergunta 02----------')
print(p2.get('Pergunta'))
print(p2.get('Opções'))
resposta_usuario_02 = input('Digite sua resposta: ')

if validacao(resposta_usuario_02) == True:    
    print('Voce acertou')
else:
    print('Resposta errada!')

print('---------Pergunta 01----------')
print(p1.get('Pergunta'))
print(p1.get('Opções'))
resposta_usuario_01 = input('Digite sua resposta: ')

if validacao(resposta_usuario_01) == True:    
    print('Voce acertou')
else:
    print('Resposta errada!')

print('---------Pergunta 03----------')
print(p2.get('Pergunta'))
print(p2.get('Opções'))
resposta_usuario_03 = input('Digite sua resposta: ')

if validacao(resposta_usuario_03) == True:    
    print('Voce acertou')
else:
    print('Resposta errada!')

