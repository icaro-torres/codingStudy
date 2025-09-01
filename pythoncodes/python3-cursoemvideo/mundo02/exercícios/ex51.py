termo_inicial = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo_termo = termo_inicial + (10 - 1) * razao
for c in range(termo_inicial, decimo_termo + razao, razao):
    print(c, end=' → ')
print('ACABOU')