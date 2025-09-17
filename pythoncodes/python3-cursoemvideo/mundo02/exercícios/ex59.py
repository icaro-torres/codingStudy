from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0
while True:
    opcao = int(input('Opções de operações:\n'
                      '[1] - somar\n'
                      '[2] - multiplicar\n'
                      '[3] - maior\n'
                      '[4] - novos números\n'
                      '[5] - sair do programa\n'
                      'Escolha uma: '))
    print('\n')

    if opcao == 1:
        soma = n1 + n2
        print('Você escolheu a soma entre os dois números.\n'
              'O resultado é {}.'.format(soma))
        print('\n')

    elif opcao == 2:
        multi = n1 * n2
        print('Você escolheu a multiplicação entre os números.\n'
              'O resultado é {}.'.format(multi))
        print('\n')
    
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Você escolheu saber qual o maior.\n'
            'Entre {} e {}, o maior é {}.'.format(n1, n2, maior))
            print('\n')
        elif n2 > n1:
            maior = n2
            print('Você escolheu saber qual o maior.\n'
              'O resultado é {}.'.format(maior))
            print('\n')
        else:
            print('Os dois números são iguais.')
            print('\n')

    
    elif opcao == 4:
        print('Você escolheu por escolher novos números.')
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite mais um número: '))
        print('\n')

    elif opcao == 5:
        print('Você optou por sair do programa.')
        break
    sleep(2)

print('Muito obriago e volte sempre!')


# solução do professor
'''
while opcao != 5:
    opcao = int(input('Opções de operações:\n'
                    '[1] - somar\n'
                    '[2] - multiplicar\n'
                    '[3] - maior\n'
                    '[4] - novos números\n'
                    '[5] - sair do programa\n'
                    'Escolha uma: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os número novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
'''