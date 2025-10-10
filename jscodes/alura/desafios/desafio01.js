// Mostre um alerta com a mensagem "Boas vindas ao nosso site!".

alert('Boas vindas ao nosso site!');

// Declare uma variável chamada nome e atribua a ela o valor "Lua".

let nome = 'Lua';

// Crie uma variável chamada idade e atribua a ela o valor 25.

let idade = 25;

// Defina uma variável numeroDeVendas e atribua a ela o valor 50.

let numeroDeVendas = 50;

// Defina uma variável saldoDisponivel e atribua a ela o valor 1000.

let saldoDisponivel = 100;

// Exiba um alerta com o texto "Erro! Preencha todos os campos"

let mensagemDeErro1 = 'Erro! Preencha todos os campos';

// Declare uma variável chamada mensagemDeErro e atribua a ela o valor "Erro! Preencha todos os campos" Agora exiba um alerta com o valor da variável mensagemDeErro.

let mensagemDeErro2 = 'Erro! Preencha todos os campos';
alert(mensagemDeErro2);

// Para o próximo código, use um novo prompt para perguntar o nome do usuário e armazená-lo em uma variável, pode chamá-la de nome ou adicionar o que desejar .

let nomeDoUsuario = prompt('Qual seu nome?');
console.log(`Olá, ${nomeDoUsuario}! Seja bem-vindo(a).`);

// Peça ao usuário para digitar sua idade usando um prompt e armazene-a na variável idade.

let idadeDoUsuario1 = prompt('Quais a sua idade?');

// Agora, para validar a idade que capturamos no desafio 09, caso a idade seja maior ou igual que 18, exiba um alerta com a mensagem "Pode tirar a habilitação!".

let idadeDoUsuario2 = prompt('Quais a sua idade?');

if (idadeDoUsuario2 >= 17) {
    alert('Pode tirar a habilitação!');
} else {
	alert('Infelizmente terá que esperar até completar 18 anos para tirar a habilitação.');
}