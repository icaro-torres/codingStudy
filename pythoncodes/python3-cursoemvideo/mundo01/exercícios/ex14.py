celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = ((9 * celsius) / 5) + 32
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(celsius, fahrenheit))

# pode ser feito também assim: 9 * celsius / 5 + 32 por causa da ordem de precedência
# ou assim: 9 / 5 * celsius + 32
# ou ainda assim: (9 * celsius + 32) / 5
# mas a primeira forma é a mais comum e recomendada
# o resultado é o mesmo