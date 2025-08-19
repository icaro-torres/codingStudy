casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
if prestacao >= salario * 0.3:
    print('O valor do empréstimo seria de R${:.2f}. Empréstimo negado!'.format(prestacao))
else:
    print('O valor do empréstimo é de R${:.2f}. Empréstimo aprovado!'.format(prestacao))