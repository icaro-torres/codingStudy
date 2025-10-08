// Crie uma função que calcule o valor do fatorial de um número passado como parâmetro.

let num = parseInt(prompt('Digite um número.'));

function calculoFatorial(num) {
    if (num < 0) {
        return 'Inválido';
    } else if (num == 0) {
        return 1;
    } else {
        return (num * calculoFatorial(num - 1));
    }
}

function mostrarCalculo(num) {
    let texto = '';

    for (let i = num; i > 0; i--) {
        texto += i;

        if (i > 1) {
            texto += ' x ';
        }
    }

    return texto;
}

if (num >= 0) {
    let resultado = calculoFatorial(num);
    let textoCalculo = mostrarCalculo(num);
    alert(`${textoCalculo} = ${resultado}.`);
} else {
    alert('Fatorial não definido para números negativos.')
}