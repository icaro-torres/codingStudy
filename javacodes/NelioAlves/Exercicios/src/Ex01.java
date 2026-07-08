import java.util.Scanner;

public class Ex01 {
    public static void main (String[] args) {

        Scanner sc = new Scanner(System.in);

        double largura = sc.nextDouble();
        double comprimento = sc.nextDouble();
        double metroQuadrado = sc.nextDouble();

        double area = largura * comprimento;
        double preco = area * metroQuadrado;

        System.out.printf("A área do imóvel é de %.2f%n", area);
        System.out.printf("O valor é %.2f%n", preco);

    }
}
