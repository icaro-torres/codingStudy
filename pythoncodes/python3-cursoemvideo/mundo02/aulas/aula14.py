# exemplos de estrutura de repetição dadas na aula apenas para entender melhor

'''while not maça:
    if chao:
        ande
    elif buraco:
        pule
    elif moeda:
        pega 
pega'''

'''for c in range(1, 10):
    print(c)
print('fim')'''

'''c = 1
while c < 10:
    c += 1
    print(c)
print('fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares.'.format(par, impar))