altura = float(input('Digite a altura da sua parede: '))
largura = float(input('Digite a largura da sua parede: '))
comprimento = altura * largura
tinta = comprimento / 2
print('Sua parede tem a dimensão {}x{} e a sua área é de {}m².'.format(altura, largura, comprimento))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))