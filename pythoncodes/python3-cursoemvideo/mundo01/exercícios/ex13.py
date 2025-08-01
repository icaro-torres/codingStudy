salario = float(input('Digite o salário: '))
porcentagem = salario * 15 / 100
# ou porcentagem = salario * 0.15
aumento = salario + porcentagem
print('O funcionário que ganhava R${:.2f}, com 15% de aumento passa a receber R${:.2f}.'.format(salario, aumento))