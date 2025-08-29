print('{:=^40}'.format(' CASAS BAHIA '))
produto = float(input('Preço do produto: R$'))
condicao = int(input('Condição de pagamento:\n'
                    '1 - À vista dinheiro/cheque (10% de desconto)\n'
                    '2 - À vista no cartão (5% de desconto)\n'
                    '3 - Em até 2x no cartão (sem juros)\n'
                    '4 - 3x ou mais no cartão (20% de juros)\n'
                    'Digite a opção desejada: '))

if condicao == 1:
    total = produto - (produto * 10 / 100)
elif condicao == 2:
    total = produto - (produto * 5 / 100)
elif condicao == 3:
    total = produto
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif condicao == 4:
    total = produto + (produto * 20 / 100)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(total_parcelas, parcela))
else:
    total = produto
    print('Opção inválida de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(produto, total))

# antes eu tinha feito assim, mas acho que ficou melhor do jeito acima
#if condicao == 1:
#    print('Valor a pagar: R${:.2f} com 10% de desconto à vista.'.format(produto * 0.9))
#elif condicao == 2:
#    print('Valor a pagar: R${:.2f} com 5% de desconto à vista no cartão.'.format(produto * 0.95))
#elif condicao == 3:
#    print('Valor a pagar: R${:.2f} em 2x de R${:.2f} sem juros'.format(produto, produto / 2))
#elif condicao == 4:
#    parcelas = int(input('Quantas parcelas? '))
#    valor_parcela = produto * 1.2 / parcelas
#    print('Valor a pagar: R${} em {}x de R${:.2f} com juros de 20%'.format(produto * 1.2, parcelas, valor_parcela))
#else:
#    print('Opção inválida. Tente novamente.')