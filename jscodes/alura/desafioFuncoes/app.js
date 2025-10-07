let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do Desafio';

function botaoConsole() {
    console.log('O botão foi cliclado.');
}

function botaoAlert() {
    alert('Eu amo JS.');
}

function botaoPrompt() {
    let cidade = prompt('Digite o nome de uma cidade do Brasil');
    alert(`Estive em ${cidade} e lembrei de você!`)
}

function botaoSoma() {
    let numero1 = prompt('Digite o primeiro número.')
    let numero2 = prompt('Digite o segundo número.')
    resultado = parseInt(numero1) + parseInt(numero2)
    alert(`A soma entre ${numero1} e ${numero2} é igual a ${resultado}.`)
}