# todo código do padrão ansi para utilizar no python é feito assim: \033[0;33;44m] sendo o 0 para style, 33 para cor do texto e 44 para cor do fundo
# exemplo de uso: print("\033[0;33;44m Olá Mundo")
# códigos de style: 0 - none; 1 - bold; 4 - underline; 7 - negative
# códigos de texto: 30 - branco; 31 - vermelho; 32 - verde; 33 - amarelo; 34 - azul; 35 - roxo; 36 - ciano; 37 - cinza
# códigos de fundo: 40 - branco; 41 - vermelho; 42 - verde; 43 - amarelo; 44 - azul; 45 - roxo; 46 - ciano; 47 - cinza

a = 3
b = 5

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))