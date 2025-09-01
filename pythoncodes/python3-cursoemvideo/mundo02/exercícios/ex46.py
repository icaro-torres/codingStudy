from time import sleep
from emoji import emojize

print('{:=^40}'.format(' CONTAGEM REGRESSIVA! '))
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize(':cone_de_festa: :cone_de_festa: :cone_de_festa: :cone_de_festa: :cone_de_festa: :cone_de_festa:', language='pt'))
print('FIIIIU... BOOM! BOOOM! BANG! POW! PAPAPAPAM! POOOOOW!')
print(emojize(':cone_de_festa: :cone_de_festa: :cone_de_festa: :cone_de_festa: :cone_de_festa: :cone_de_festa:', language='pt'))