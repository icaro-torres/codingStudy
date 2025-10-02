var numero = parseFloat(prompt('Digite um número.'));

if (numero > 0){
    alert(`Você digitou ${numero} que é um número positivo.`);
} else if (numero < 0) {
    alert(`Você digitou ${numero} que é um número negativo.`);
} else {
    alert('Esse número é 0.');
}
