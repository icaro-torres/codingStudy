// Crie uma função que converte um valor em dólar, passado como parâmetro, e retorna o valor equivalente em reais. Para isso, considere a cotação do dólar igual a R$4,80.

let valorDolar = parseFloat(prompt('Digite o valor que deseja converter.'));

function convercaoDolar(valorDolar) {
    valorReais = valorDolar * 4.80;
    return valorReais;
}

let valorFinal = convercaoDolar(valorDolar);
alert(`O valor US$${valorDolar} fica R$${valorFinal}.`);