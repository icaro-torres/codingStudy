import java.util.Scanner;

public class Ex03 {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);

        double raioCirculo = sc.nextDouble();

        double pi = 3.14159;

        double areaCirculo = (pi * raioCirculo) * raioCirculo;

        System.out.printf("A área do círculo é %.4f%n", areaCirculo);
    }
}
