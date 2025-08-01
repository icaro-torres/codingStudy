n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

# o \n é usado pra criar linha sem precisar usar outro comando print e o end='' é quando você quer dar outro print, mas não quer uma quebra de linhas.
# o :.3f é pra formatar a quantidade de números após a vírgula (ponto flutuante), no caso ali são 3 casas decimais que serão exibidas.