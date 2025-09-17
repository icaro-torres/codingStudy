from random import randint
from time import sleep

numero = randint(0, 10)
nome = input('Qual é o seu nome? ')

print('\n')
print('-' * 50)
print('Olá, {}! Bem-vindo/a ao jogo de adivinhação.'.format(nome))
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')
print('-' * 50)
print('\n')

palpite = 0

while True:
    aposta = int(input('Qual número eu pensei? '))

    print('\n')
    print('Você apostou no número {}.'.format(aposta))
    print('Sorteando um número entre 0 e 10...')
    sleep(2)  # pausa para aumentar a expectativa
    print('\n')

    if numero != aposta:
        print('OPA! Você perdeu, {}! Sua aposta foi {}. Tente mais uma vez.'.format(nome, aposta))
        print('\n')
        palpite += 1
    elif aposta == numero:
        print('PARABÉNS! Você ganhou, {}! Eu pensei em {}!'.format(nome, numero))
        print('\n')
        break
print('Você precisou de {} tentativas.'.format(palpite))