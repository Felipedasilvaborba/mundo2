from random import randint
from time import sleep
lista = ('PEDRA','PAPEL','TESOURA')
computador = randint(0, 2)
print('Suas opções: ')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-=-=-=-=-=-=-=-=-=-=-=-=')
print('Sua jogada foi {}'.format(lista[jogador]))
print('Jogada do computador {}'.format(lista[computador])) 
print('-=-=-=-=-=-=-=-=-=-=-=-=')
if jogador == 0 and computador == 2:
    print('JOGADOR VENCE!!')
elif jogador == 0 and computador == 1:
    print('COMPUTADOR VENCE!!')
elif jogador == 1 and computador == 0:
    print('JOGADOR VENCE!!')
elif jogador == 1 and computador == 2:
    print('COMPUTADOR VENCE!!')
elif jogador == 2 and computador == 1:
    print('JOGADOR VENCE!!')
elif jogador == 2 and computador == 0:
    print('COMPUTADOR VENCE!!')
else:
    print('EMPATE!!')