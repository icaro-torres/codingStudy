nome = str(input('Digite seu nome: '))
peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura ** 2)

print('Olá, {}, seu IMC é {:.1f}.'.format(nome, imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade, cuidado.')
else:
    print('Você está com obesidade \033[31mGRAVE\033[m, cuidado!')