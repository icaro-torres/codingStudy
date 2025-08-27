nome = str(input('Digite o nome do aluno: ')).strip()
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('O aluno {} foi \033[31mREPROVADO\033[m com média {:.1f}.'.format(nome, media))
elif media >= 5 and media < 7:
    print('O aluno {} está de \033[33mRECUPERAÇÃO\033[m com média {:.1f}.'.format(nome, media))
elif media >= 7.0:
    print('O aluno {} foi \033[32mAPROVADO\033[m com média {:.1f}.'.format(nome, media))