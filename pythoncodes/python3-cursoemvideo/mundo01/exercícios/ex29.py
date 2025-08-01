km = float(input('Você está rodando a quantos km/h? '))

if km > 80:
    multa = (km - 80) * 7
    print('Você excedeu o limite de velocidade e deve pagar uma multa de R${:.2f}.'.format(multa))
print('Tenha um bom dia e continue com segurança!')