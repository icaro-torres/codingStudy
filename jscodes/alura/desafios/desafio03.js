// Crie um contador que comece em 1 e vá até 10 usando um loop while. Mostre cada número.

let contador1 = 1;

while (contador1 < 11) {
    console.log(`${contador1}`);
    contador1 ++;
}

// Crie um contador que começa em 10 e vá até 0 usando um loop while. Mostre cada número.

let contador2 = 10;

while (contador2 > 0) {
    console.log(`${contador2}`);
    contador2 --;
}

// Crie um programa de contagem regressiva. Peça um número e conte deste número até 0, usando um loop while no console do navegador.

let numero1 = prompt('Escolha um número!');
let contagemRegressiva1 = numero1

while (contagemRegressiva1 > 0) {    
    console.log(`${contagemRegressiva1}`);
    contagemRegressiva1 --;
}

// Crie um programa de contagem progressiva. Peça um número e conte de 0 até esse número, usando um loop while no console do navegador.

let numero2 = prompt('Escreva um número.');
let contagemRegressiva2 = 0;

while (contagemRegressiva2 <= numero2) {
    console.log(`${contagemRegressiva2}`);
    contagemRegressiva2 ++;
}