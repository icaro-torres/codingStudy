termo_inicial = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo_atual = termo_inicial
contador = 0

print('-' * 10, '\nProgressão aritmética:')

while contador < 10:
    print(termo_atual, end=', ')
    termo_atual += razao
    contador += 1
print('Fim.')