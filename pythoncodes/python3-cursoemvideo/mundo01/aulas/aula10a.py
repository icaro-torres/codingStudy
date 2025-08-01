tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo.')
else:
    print('Carro velho.')
print('--- Fim! ---')


# também dá pra fazer com print('Carro novo.' if tempo <= 3 else 'Carro velho.'), mas fica menos legível e, se você não tem experiência, pode ser confuso.