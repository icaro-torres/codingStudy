numero_primo = int(input('Digite um número: '))
contador = 0

for c in range(1, numero_primo + 1):
    if numero_primo % c == 0:
        print('\033[34m{}'.format(c), end=' ')
        contador += 1
    else:
        print('\033[31m{}'.format(c), end=' ')

if contador == 2:
    print('\n\033[mO número {} é primo, pois foi divisível {} vezes!'.format(numero_primo, contador))
else:
    print('\n\033[mO número {} não é primo, pois foi divisível {} vezes!'.format(numero_primo, contador))