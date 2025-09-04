from datetime import date

ano_atual = date.today().year
menores = 0
maiores = 0

for i in range(1, 8):
    ano_nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    idade = ano_atual - ano_nascimento
    if idade <= 17:
        menores += 1
    elif idade >= 18:
        maiores += 1

print('Ao todo tivemos {} pessoas maiores de idade.'.format(maiores))
print('E também tivemos {} pessoas menores de idade.'.format(menores))