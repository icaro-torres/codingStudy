viagem = float(input('Qual a distância da sua viagem em km? '))

if viagem > 200:
    valor = viagem * 0.45
    print('Você pagará R${:.2f} por essa viagem.'.format(valor))
else:
    valor2 = viagem * 0.50
    print('Você pagará R${:.2f} por essa viagem.'.format(valor2))

# dá pra fazer também com peço = viagem * 0.50 if viagem <= 200 else viagem * 0.45