produto = float(input('Preço do produto: R$'))
condicao = int(input('Condição de pagamento:\n'
                    '1 - À vista dinheiro/cheque (10% de desconto)\n'
                    '2 - À vista no cartão (5% de desconto)\n'
                    '3 - Em até 2x no cartão (sem juros)\n'
                    '4 - 3x ou mais no cartão (20% de juros)\n'
                    'Digite a opção desejada: '))

if condicao == 1:
    print(f'Valor a pagar: R${produto * 0.9:.2f}')
elif condicao == 2:
    print(f'Valor a pagar: R${produto * 0.95:.2f}')
elif condicao == 3:
    print(f'Valor a pagar: R${produto:.2f} em 2x de R${produto / 2:.2f}')
elif condicao == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor_parcela = produto * 1.2 / parcelas
    print(f'Valor a pagar: R${produto * 1.2:.2f} em {parcelas}x de R${valor_parcela:.2f}')
else:
    print('Opção inválida. Tente novamente.')