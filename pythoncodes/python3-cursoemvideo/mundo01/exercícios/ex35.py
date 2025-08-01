a = float(input('Diga o comprimento da primeira reta: '))
b = float(input('Diga o comprimento da segunda reta: '))
c = float(input('Diga o comprimento da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')