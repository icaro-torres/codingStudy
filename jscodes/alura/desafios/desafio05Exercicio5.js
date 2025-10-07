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