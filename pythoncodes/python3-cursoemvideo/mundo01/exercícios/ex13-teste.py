salario = float(input('Digite o salário: R$'))
porcentagem = int(input('Digite a porcentagem de aumento (somente números inteiros): '))
novo_salario = salario * porcentagem / 100
aumento = salario + novo_salario
print('O funcionário que receberia R${:.2f}, com {}% de aumento passa a receber R${:.2f}.'.format(salario, porcentagem, aumento))