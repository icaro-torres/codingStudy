a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
if a > b:
    print('O valor {} é maior que {}.'.format(a, b))
elif b > a:
    print('O valor {} é maior que {}.'.format(b, a))
else:
    print('Não existe valor maior, os dois números são iguais.')