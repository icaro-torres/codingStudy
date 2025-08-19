nome = str(input('Digite o nome do aluno: ')).strip()
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('O aluno {} foi \033[31mREPROVADO\033[m com média {:.1f}.'.format(nome, media))
elif media >= 5.0 and media < 6.9:
    print('O aluno {} está de \033[33mRRECUPERAÇÃO\033[m com média {:.1f}.'.format(nome, media))
elif media >= 7.0:
    print('O aluno {} foi \033[32mRAPROVADO\033[m com média {:.1f}.'.format(nome, media))