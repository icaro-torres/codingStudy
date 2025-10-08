// Crie uma função que calcule o índice de massa corporal (IMC) de uma pessoa, a partir de sua altura, em metros, e peso, em quilogramas, que serão recebidos como parâmetro.

// o cálculo de IMC é feito divindo o peso (em kg) pela altura ao quadrado (em metros). a formula seria IMC = peso / (altura x altura)

let altura = parseFloat(prompt('Digite sua altura.'))
let peso = parseFloat(prompt('Digite seu peso.'))

function calculaIMC(peso, altura) {
     IMC = peso / (altura * altura);
    let classificacao;

    if (IMC < 18.5) {
        classificacao = 'Magreza';
    } else if (IMC < 25) {
        classificacao = 'Normal';
    } else if (IMC <30) {
        classificacao = 'Sobrepeso';
    } else if (IMC < 35) {
        classificacao = 'Obesidade grau I';
    } else if (IMC < 40) {
        classificacao = 'Obesidade grau II';
    } else {
        classificacao = 'Obesidade grau III';
    }

    alert(`Seu IMC é ${IMC.toFixed(2)}, isso significa ${classificacao}.`)
}

calculaIMC(peso, altura);