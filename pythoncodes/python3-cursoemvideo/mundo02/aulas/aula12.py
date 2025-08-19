nome = str(input('Digite seu nome completo: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Ana Clara Maria Jéssica':
    print('Belo nome feminino!')
else: # lembrando que o else é opcional
    print('Seu nome é bem normal!')
print('Tenha um ótimo dia, {}!'.format(nome))