n = int(input('Digite um número: '))
opcao = int(input('''Escolha uma das bases para conversão:
                  [1] para BINÁRIO
                  [2] para OCTAL
                  [3] para HEXADECIMAL
                  Sua opção: '''))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:].upper()))
else:
    print('Opção inválida. Tente novamente.')