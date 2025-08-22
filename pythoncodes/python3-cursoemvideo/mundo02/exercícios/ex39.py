from datetime import date

ano = date.today().year
nascido = int(input('Informe o ano do seu nascimento: '))
idade = ano - nascido

print('Quem nasceu em {} tem {} anos em {}.'.format(nascido, idade, ano))

if idade < 18:
    saldo = 18 - idade
    print('Você ainda irá se alistar ao serviço militar. Faltam {} anos.'.format(saldo))
    print('Seu alistamento será em {}.'.format(ano + saldo))
elif idade == 18:
    print('Você deve se alistar ao serviço militar imediatamente.')
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado ao serviço militar há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(ano - saldo))
