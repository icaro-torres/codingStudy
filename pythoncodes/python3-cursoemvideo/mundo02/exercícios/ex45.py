from random import randint
from time import sleep

computador = randint(1, 3)  # 1: Pedra, 2: Papel, 3: Tesoura

print('Escola uma opção:\n'
    '[1] Pedra\n'
    '[2] Papel\n'
    '[3] Tesoura\n'
    '[4] Sair do jogo')
escolha = int(input('Sua escolha: '))

if escolha not in [1, 2, 3, 4]:
    print('Opção inválida! Tente novamente.')
elif escolha == 4:
    print('Saindo do jogo. Até mais!')
elif escolha == 1:
    jogador = 'Pedra'
elif escolha == 2:
    jogador = 'Papel'
elif escolha == 3:
    jogador = 'Tesoura'

print(f'Você escolheu: {jogador}')
print(f'Eu escolhi: {["Pedra", "Papel", "Tesoura"][computador - 1]}')

if computador == escolha:
    print('Empate!')
elif (computador == 1 and escolha == 3) or (computador == 2 and escolha == 1) or (computador == 3 and escolha == 2):
    print('Você perdeu!')
else:
    print('Você ganhou!')