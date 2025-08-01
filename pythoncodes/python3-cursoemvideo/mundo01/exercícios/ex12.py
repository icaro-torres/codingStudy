valor_orig = float(input('Digite o valor do produto: R$'))
novo_valor = valor_orig * 5 / 100
print('O desconto de 5% de R${} é R${:.2f}. O valor na promoção fica R${:.2f}'.format(valor_orig, novo_valor, valor_orig - novo_valor))