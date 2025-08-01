salario = float(input('Digite o salário do funcionário: R$'))
nome = str(input('Digite o nome do funcionário: '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O funcionário {} ganhava {:.2f} e passa a receber R${:.2f} com aumento.'.format(nome, salario, novo))