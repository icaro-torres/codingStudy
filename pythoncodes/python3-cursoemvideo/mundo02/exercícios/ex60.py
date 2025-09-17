# versão simplificada do professor
from math import factorial

n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

n = int(input('Digite um número: '))
resultado = 1

# versão usando while
count = 1

while count <= n:
    resultado *= count
    count += 1
print('O fatorial de {} é {}.'.format(n, resultado))

# versão usando for
for c in range(1, n+1):
    resultado *= c
print('O fatorial de {} é {}.'.format(n, resultado))

# versão completa do professor
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))