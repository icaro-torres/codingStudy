// Criar uma função que exibe "Olá, mundo!" no console.

function saudacao() {
    console.log('Olá, mundo!');
}
saudacao();

// Criar uma função que recebe um nome como parâmetro e exibe "Olá, [nome]!" no console.

function saudacoes() {
    let nomeDoUsuario = prompt('Qual seu nome?');
    console.log(`Olá, ${nomeDoUsuario}. Bem-vindo!`);
}
saudacoes();

// Criar uma função que recebe um número como parâmetro e retorna o dobro desse número.

function multiplicarNumero() {
    let numero = parseInt(prompt('Digite um número!'));
    resultado = numero * 2;
    alert(`${numero} x 2 = ${resultado}.`);
}
multiplicarNumero();

// Criar uma função que recebe três números como parâmetros e retorna a média deles.

function mediaNumeros() {
    let num1 = parseInt(prompt('Digite o primeiro número.'));
    let num2 = parseInt(prompt('Digite o segundo número.'));
    let num3 = parseInt(prompt('Digite o terceiro número.'));
    media = (num1 + num2 + num3) / 3;
    alert(`A media entre ${num1}, ${num2} e ${num3} é ${media}.`);
}
mediaNumeros();

// Criar uma função que recebe dois números como parâmetros e retorna o maior deles.

function verificarMaior() {
    let num1 = parseInt(prompt('Digite o primeiro número.'));
    let num2 = parseInt(prompt('Digite o segundo número.'));
    if (num1 > num2) {
        alert(`O número ${num1} é o maior.`);
    } else {
        alert(`O número ${num2} é o maior.`);
    }
}
verificarMaior();

// Criar uma função que recebe um número como parâmetro e retorna o resultado da multiplicação desse número por ele mesmo

function multiplicarNumero() {
    let numero = parseInt(prompt('Digite um número.'));
    resultado = numero * numero;
    alert(`${numero} x ${numero} = ${resultado}.`);
}
multiplicarNumero();