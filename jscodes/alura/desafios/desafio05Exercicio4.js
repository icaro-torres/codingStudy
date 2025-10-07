function mediaNumeros() {
    let num1 = parseInt(prompt('Digite o primeiro número.'));
    let num2 = parseInt(prompt('Digite o segundo número.'));
    let num3 = parseInt(prompt('Digite o terceiro número.'));
    media = (num1 + num2 + num3) / 3;
    alert(`A media entre ${num1}, ${num2} e ${num3} é ${media}.`);
}
mediaNumeros();