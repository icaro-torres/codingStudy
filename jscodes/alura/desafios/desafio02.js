// Pergunte ao usuário qual é o dia da semana. Se a resposta for "Sábado" ou "Domingo", mostre "Bom fim de semana!". Caso contrário, mostre "Boa semana!".

let diaDaSemana = prompt('Que dia da semana é hoje?');

if (diaDaSemana == 'Sábado' && diaDaSemana == 'Domingo') {
    alert('Bom fim de semana!');
} else {
    alert('Boa semana!');
}

// Verifique se um número digitado pelo usuário é positivo ou negativo. Mostre um alerta informando.

let numero = prompt('Digite um número');

if (numero >= 0) {
    alert(`O número ${numero} é positivo!`);
} else {
    alert(`O número ${numero} é negativo!`);
}

// Crie um sistema de pontuação para um jogo. Se a pontuação for maior ou igual a 100, mostre "Parabéns, você venceu!". Caso contrário, mostre "Tente novamente para ganhar.".

pontosDoJogador = 130;

if (pontosDoJogador >= 100) {
    console.log('Parabéns, você venceu!');
} else {
    console.log('Tente novamente para ganhar.');
}

// Crie uma mensagem que informa o usuário sobre o saldo da conta, usando uma template string para incluir o valor do saldo.

let saldoDaConta = prompt('Qual o saldo de sua conta?');
alert(`O saldo da conta informado foi: R$${saldoDaConta}.`);

// Peça ao usuário para inserir seu nome usando prompt. Em seguida, mostre um alerta de boas-vindas usando esse nome.

let nomeDoUsuario = prompt('Digite seu nome.');
alert(`Olá, ${nomeDoUsuario}. Seja bem-vindo!`);