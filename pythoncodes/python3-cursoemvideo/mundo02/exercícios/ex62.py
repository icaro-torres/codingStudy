'''termo_inicial = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
num_termos = int(input('Quantos termos você quer gerar?: '))

termo_atual = termo_inicial
contador = 0

print('\nProgressão aritmética:')

while contador < num_termos:
    print(termo_atual, end=', ')
    termo_atual += razao
    contador += 1
print('Fim.')'''

# eu esqueci que tinha que ir perguntando quantos mais até o usuário digitar 0,
# então esse é o correto:

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}, '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'. format(total))