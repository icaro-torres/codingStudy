n = quantidade = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para sair]: '))
    if n != 999:
        quantidade += 1
        soma += n
print('Você digitou {} números e a soma entre eles é {}.'.format(quantidade, soma))