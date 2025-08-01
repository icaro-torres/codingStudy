real = float(input('Quanto dinheiro você tem? R$'))
dolar = real / 5.44
euro = real / 6.38
iene = real / 0.037
print('Seus R${} ficarão {:.2f} ienes.'.format(real, iene))
print('Seus R${} ficarão {:.2f} euros.'.format(real, euro))
print('Seus R${} ficarão {:.2f} dólares.'.format(real, dolar))