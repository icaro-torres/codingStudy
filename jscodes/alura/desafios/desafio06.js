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

// Crie uma função que calcule o valor do fatorial de um número passado como parâmetro.

let num = parseInt(prompt('Digite um número.'));

function calculoFatorial(num) {
    if (num < 0) {
        return 'Inválido';
    } else if (num == 0) {
        return 1;
    } else {
        return (num * calculoFatorial(num - 1));
    }
}

function mostrarCalculo(num) {
    let texto = '';

    for (let i = num; i > 0; i--) {
        texto += i;

        if (i > 1) {
            texto += ' x ';
        }
    }

    return texto;
}

if (num >= 0) {
    let resultado = calculoFatorial(num);
    let textoCalculo = mostrarCalculo(num);
    alert(`${textoCalculo} = ${resultado}.`);
} else {
    alert('Fatorial não definido para números negativos.')
}

// Crie uma função que converte um valor em dólar, passado como parâmetro, e retorna o valor equivalente em reais. Para isso, considere a cotação do dólar igual a R$4,80.

let valorDolar = parseFloat(prompt('Digite o valor que deseja converter.'));

function convercaoDolar(valorDolar) {
    valorReais = valorDolar * 4.80;
    return valorReais;
}

let valorFinal = convercaoDolar(valorDolar);
alert(`O valor US$${valorDolar} fica R$${valorFinal}.`);

// Crie uma função que mostre na tela a área e o perímetro de uma sala retangular, utilizando altura e largura que serão dadas como parâmetro.

let altura1 = parseFloat(prompt('Digite a altura desejada.'))
let largura = parseFloat(prompt('Digite a largura desejada.'))

function calculoSalaRetangular(altura1, largura) {
    let perimetro = 2 * (altura1 + largura);
    let area = altura1 * largura;
    alert(`O perímetro é de ${perimetro} e a área é de ${area}.`)
}

calculoSalaRetangular(altura1, largura);

// Crie uma função que mostre na tela a área e o perímetro de uma sala circular, utilizando seu raio que será fornecido como parâmetro. Considere Pi = 3,14.

let raio = parseFloat(prompt('Digite um número.'));

function salaCircular(raio) {
    perimetro = 2 * 3.14 * raio;
    area = (raio * raio) * 3.14;
    alert(`A área é ${area.toFixed(2)} e o perímetro é ${perimetro.toFixed(2)}.`)
}

salaCircular(raio);

// Crie uma função que mostre na tela a tabuada de um número dado como parâmetro.

let num1 = parseInt(prompt('Digite um número.'));
let numFinal = parseInt(prompt('Até que número você quer a tabuada?'));

function mostrarTabuada(num1, numFinal) {
    for (let i = 1; i <= numFinal; i++) {
        tabuada = num1 * i;
        console.log(`${num1} x ${i} = ${tabuada}.`);
    }
}

mostrarTabuada(num1, numFinal);