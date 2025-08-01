import math
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipo = pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)
hipotenusa = math.sqrt(hipo)
print('O cateto oposto é {}, o cateto adjacente é {} e a hipotenusa é {:.2f}'.format(cateto_oposto, cateto_adjacente, hipotenusa))

# também dá pra fazer hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2) sem usar a biblioteca math
# ou hipotenusa = math.hypot(cateto_oposto, cateto_adjacente) que é mais simples