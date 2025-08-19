a = float(input('Diga o comprimento da primeira reta: '))
b = float(input('Diga o comprimento da segunda reta: '))
c = float(input('Diga o comprimento da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if a == b == c:
        print('O triângulo é EQUILÁTERO!')
    elif a == b or a == c or b == c:
        print('O triângulo é ISÓSCELES!')
    else:
        print('O triângulo é ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')