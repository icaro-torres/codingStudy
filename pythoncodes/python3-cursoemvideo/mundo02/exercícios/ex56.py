idade_total = 0
idade_mulheres = 0
homem_mais_velho = ''
idade_mais_velho = 0

for i in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    sexo = str(input('Digite o sexo da {}ª pessoa [M/F]: '.format(i))).upper()
    idade_total += idade

    if sexo == "M" and idade >= idade_mais_velho:
        homem_mais_velho = nome
        idade_mais_velho = idade
    elif sexo == "F" and idade < 20:
        idade_mulheres += 1

media_idades = idade_total / 4
print('A média entre as idades é de {}.'.format(media_idades))
print('O homem mais velho é {} e sua idade é {}.'.format(homem_mais_velho, idade_mais_velho))
print('Temos {} mulheres com menos de 20 anos.'.format(idade_mulheres))