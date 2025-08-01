a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a > b and a > c:
    print('O maior número é {}.'.format(a))
    print('O menor número é {}.'.format(min(b, c)))
elif b > a and b > c:
    print('O maior número é {}.'.format(b))
    print('O menor número é {}.'.format(min(a, c)))
elif c > a and c > b:
    print('O maior número é {}.'.format(c))
    print('O menor número é {}.'.format(min(a, b)))

# esse exercício dá pra fazer usando listas também e random.sort() para ordenar os números