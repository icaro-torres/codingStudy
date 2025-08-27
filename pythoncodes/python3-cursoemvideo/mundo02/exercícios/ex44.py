produto = float(input('Preço do produto: R$'))
condicao = int(input('Condição de pagamento:\n'
                    '1 - À vista dinheiro/cheque (10% de desconto)\n'
                    '2 - À vista no cartão (5% de desconto)\n'
                    '3 - Em até 2x no cartão (sem juros)\n'
                    '4 - 3x ou mais no cartão (20% de juros)\n'
                    'Digite a opção desejada: '))

if condicao == 1:
    print('Valor a pagar: R${:.2f} com 10% de desconto à vista.'.format(produto * 0.9))
elif condicao == 2:
    print('Valor a pagar: R${:.2f} com 5% de desconto à vista no cartão.'.format(produto * 0.95))
elif condicao == 3:
    print('Valor a pagar: R${:.2f} em 2x de R${:.2f} sem juros'.format(produto, produto / 2))
elif condicao == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor_parcela = produto * 1.2 / parcelas
    print('Valor a pagar: R${} em {}x de R${:.2f} com juros de 20%'.format(produto * 1.2, parcelas, valor_parcela))
else:
    print('Opção inválida. Tente novamente.')