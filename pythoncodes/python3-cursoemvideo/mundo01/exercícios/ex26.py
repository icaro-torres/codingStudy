frase = input('Digite uma frase: ').strip().lower()
print('A letra "a" aparece {} vezes na frase.'.format(frase.count('a')))
print('Aparece pela primeira vez na posição {}.'.format(frase.find('a') + 1))
print('Aparece pela última vez na posição {}.'.format(frase.rfind('a') + 1))