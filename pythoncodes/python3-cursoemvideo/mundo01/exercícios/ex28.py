from random import randint
from time import sleep

numero = randint(0, 5)
nome = input('Qual é o seu nome? ')

print('\n')
print('-' * 50)
print('Olá, {}! Bem-vindo/a ao jogo de adivinhação.'.format(nome))
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('-' * 50)
print('\n')

aposta = int(input('Qual número eu pensei? '))

print('\n')
print('Você apostou no número {}.'.format(aposta))
print('Sorteando um número entre 0 e 5...')
sleep(5)  # pausa para aumentar a expectativa
print('\n')

if numero == aposta:
    print('PARABÉNS! Você ganhou, {}!'.format(nome))
else:
    print('OPA! O número que pensei foi {}. Você perdeu, {}! Tente mais uma vez.'.format(numero, nome))