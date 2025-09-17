# eu tinha feito dessa forma:

'''sexo = ''
while True:
    pergunta = str(input('Qual seu sexo? [F/M]: ')).upper().strip()[0]
    if pergunta == 'F' or pergunta == 'M':
        sexo = pergunta
        break
    elif pergunta != 'F' or pergunta != 'M':
        print('Dado incorreto, tente novamente.')
print('O sexo {} validado com sucesso.'.format(sexo))'''

# achei melhor a do professor:

sexo = str(input('Informe seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [F/M]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))