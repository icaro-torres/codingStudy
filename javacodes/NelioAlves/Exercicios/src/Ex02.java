import java.util.Scanner;

public class Ex02 {
    public static void main (String[] args) {

        Scanner sc = new Scanner(System.in);

        int primeiroNumero, segundoNumero;

        primeiroNumero = sc.nextInt();
        segundoNumero = sc.nextInt();

        int soma = primeiroNumero + segundoNumero;

        System.out.println("A soma é: " + soma);

    }
}
