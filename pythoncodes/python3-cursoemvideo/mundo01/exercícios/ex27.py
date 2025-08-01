nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome completo é: {}. \nSeu primeiro nome é: {}. \nSeu último nome é: {}'.format(nome, nome.split()[0], nome.split()[-1]))

# pra pegar o último também dá pra usar .format(nome[len(nome)-1])