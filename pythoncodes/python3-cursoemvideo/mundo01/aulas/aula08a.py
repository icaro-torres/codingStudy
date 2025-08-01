# se usar impot biblioteca, ele vai me trazer tudo que tem na biblioteca, sendo mais generalista
# se usar from biblioteca import funcao, ele vai me trazer apenas a funcao, sendo mais especifico
# se usar from biblioteca import funcao as f, ele vai me trazer a funcao com o apelido f
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) arredonda para baixo
# print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) arredonda para cima
# print('A raiz de {} é igual a {}'.format(num, math.trunc(raiz))) elimina a parte decimal
# print('A raiz de {} é igual a {:.2f}'.format(num, math.pow(num, (1/2)))) outra forma de calcular a raiz quadrada