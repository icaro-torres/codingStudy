// Crie uma função que mostre na tela a área e o perímetro de uma sala retangular, utilizando altura e largura que serão dadas como parâmetro.

let altura = parseFloat(prompt('Digite a altura desejada.'))
let largura = parseFloat(prompt('Digite a largura desejada.'))

function calculoSalaRetangular(altura, largura) {
    let perimetro = 2 * (altura + largura);
    let area = altura * largura;
    alert(`O perímetro é de ${perimetro} e a área é de ${area}.`)
}

calculoSalaRetangular(altura, largura);