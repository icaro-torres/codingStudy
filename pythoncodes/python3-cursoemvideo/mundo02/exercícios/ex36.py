casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
if prestacao >= salario * 0.3:
    print('Para pagar {} em {} anos, a prestação empréstimo será de R${:.2f}. Empréstimo negado!'.format(casa, anos, prestacao))
else:
    print('Para pagar {} em {} anos, a prestação empréstimo será de R${:.2f}. Empréstimo aprovado!'.format(casa, anos, prestacao))