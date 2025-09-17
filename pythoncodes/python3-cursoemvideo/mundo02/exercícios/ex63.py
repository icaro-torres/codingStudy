n = int(input('Digite um número: '))
contador = 0
a = 0
b = 1

while contador < n:
    print('{} -> '.format(a), end='')
    novo = a + b
    a = b
    b = novo
    contador += 1
print('Fim.')