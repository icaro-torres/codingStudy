num = input('Digite um número (de 0 a 9999): ').zfill(4) # preenche com zeros à esquerda
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))

# dá pra fazer com número inteiros também, tipo num // 1 % 10, num // 10 % 10, num // 100 % 10 e por aí vai