from math import sin, cos, tan, radians
angulo_graus = float(input('Digite o ângulo em graus: '))
angulo_radianos = radians(angulo_graus)
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)
print('O angulo de {} graus tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}'.format(angulo_graus, seno, cosseno, tangente))

# dá pra fazer direto, sem tranformar em radianos primeiro, fica tipo: seno = sin(radians(angulo_graus))