public class Aula2 {
    public static void main(String[] args) {

        // Exercício 1
        double nota1 = 8.0;
        double nota2 = 7.0;
        double media = (nota1 + nota2) / 2;
        System.out.println(media);

        // Exercício 2
        double um = 5.0;
        int dois;
        dois = (int) um;
        System.out.println(dois);

        // Exercício 3
        char letra = 'A';
        String letra1 = ", oi!";
        System.out.println(letra + letra1);

        // Exercício 4
        double precoProduto = 25.50;
        int quantidade = 20;
        double valorTotal = precoProduto * quantidade;
        System.out.println("O valor total fica: " + valorTotal);

        // Exercício 5
        double produto = 100.0;
        double valorEmDolar = 5.50;
        double conversao = produto * valorEmDolar;
        System.out.println("O valor em convertido: " + conversao);
    }
}