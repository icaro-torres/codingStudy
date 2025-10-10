// Crie um programa que utilize o console.log para exibir uma mensagem de boas-vindas.

let nomeJogador = prompt('Diga seu nome!');
console.log(`Boas vindas, jogador ${nomeJogador}!`);

// Crie uma variável chamada "nome" e atribua a ela o seu nome. Em seguida, utilize o console.log para exibir a mensagem "Olá, [seu nome]!" no console do navegador.

let nome1 = 'Ícaro Torres';
console.log(`Olá! ${nome1}`);

// Crie uma variável chamada "nome" e atribua a ela o seu nome. Em seguida, utilize o alert para exibir a mensagem "Olá, [seu nome]!" .

let nome2 = 'Ícaro';
alert(`Olá, ${nome2}`);

// Utilize o prompt e faça a seguinte pergunta: Qual a linguagem de programação que você mais gosta?. Em seguida, armazene a resposta em uma variável e mostre no console do navegador.

let escolhaLinguagem = prompt('Qual linguagem de programação você mais gosta?');
console.log(`Você escolheu a linguagem ${escolhaLinguagem}!`);

// Crie uma variável chamada "valor1" e outra chamada "valor2", atribuindo a elas valores numéricos de sua escolha. Em seguida, realize a soma desses dois valores e armazene o resultado em uma terceira variável chamada "resultado". Utilize o console.log para mostrar a mensagem "A soma de [valor1] e [valor2] é igual a [resultado]." no console.

let valor1 = 10;
let valor2 = 20;
let resultado = valor1 + valor2;
console.log(`A soma de ${valor1} e ${valor2} é igual a ${resultado}`);

// Crie uma variável chamada "valor1" e outra chamada "valor2", atribuindo a elas valores numéricos de sua escolha. Em seguida, realize a subtração desses dois valores e armazene o resultado em uma terceira variável chamada "resultado". Utilize o console.log para mostrar a mensagem "A diferença entre [valor1] e [valor2] é igual a [resultado]." no console.

let valor3 = 58;
let valor4 = 43;
let resultado1 = valor3 - valor4;
console.log(`A diferença entre ${valor3} e ${valor4} é a igual a ${resultado1}`);

// Peça ao usuário para inserir sua idade com prompt. Com base na idade inserida, utilize um if para verificar se a pessoa é maior ou menor de idade, exibindo uma mensagem apropriada no console.

let idadeUsuario = prompt('Digite sua idade.');

if (idadeUsuario > 17) {
    alert(`Você tem ${idadeUsuario} anos, portanto é maior de idade.`);
} else {
    alert(`Você tem ${idadeUsuario} anos, portanto é menor de idade.`);
}

// Crie uma variável "numero" e peça um valor com prompt verifique se é positivo, negativo ou zero. Use if-else para imprimir a respectiva mensagem.

var numero = parseFloat(prompt('Digite um número.'));

if (numero > 0){
    alert(`Você digitou ${numero} que é um número positivo.`);
} else if (numero < 0) {
    alert(`Você digitou ${numero} que é um número negativo.`);
} else {
    alert('Esse número é 0.');
}

// Use um loop while para imprimir os números de 1 a 10 no console.

let countdown = 1;
while (countdown <= 10) {
    console.log(countdown);
    countdown ++;
}

// Crie uma variável "nota" e atribua um valor numérico a ela. Use if-else para determinar se a nota é maior ou igual a 7 e exiba "Aprovado" ou "Reprovado" no console.

let nota = prompt(`Digite sua nota.`);

if (nota >= 7) {
    console.log(`Sua nota é ${nota} e você está aprovado!`);
} else {
    console.log(`Sua nota é ${nota} e você está reprovado!`);
}

// Use o Math.random para gerar qualquer número aleatório e exiba esse número no console.

let numeroAleatorio = Math.random();
console.log(numeroAleatorio);

// Use o Math.random para gerar um número inteiro entre 1 e 10 e exiba esse número no console.

let numeroAleatorio1 = parseInt(Math.random() * 10)+ 1;
console.log(numeroAleatorio1);

// Use o Math.random para gerar um número inteiro entre 1 e 1000 e exiba esse número no console.

let numeroAleatorio2 = parseInt(Math.random() * 1000) + 1;
console.log(numeroAleatorio2);