soma = 0
for p in range(7 -1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares é {}'.format(soma))