for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('Acabou!')

# pra ficar menor o número de iterações no laço, fica melhor fazer é 
# for c in range(2, 51, 2), o primeiro número é o começo, o segundo o final e o 
# terceiro é a quantidade ou qual é o passo