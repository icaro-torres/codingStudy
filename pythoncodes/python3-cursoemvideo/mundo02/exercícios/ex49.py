num = int(input('Digite um número: '))
tabuada = int(input('Até que número você quer a tabuada? '))

for n in range(1, tabuada + 1):
    print('{} x {:2} = {}'.format(num, n, num * n))