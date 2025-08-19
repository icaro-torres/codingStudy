from datetime import date

nascido = int(input('Informe o ano do seu nascimento: '))
ano = date.today().year
idade = ano - nascido

if idade < 18:
    print('Você ainda irá se alistar ao serviço militar. Faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('Você deve se alistar ao serviço militar este ano.')
elif idade > 18:
    print('Você já deveria ter se alistado ao serviço militar há {} anos.'.format(idade - 18))