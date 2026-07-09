import java.util.Scanner;

public class Ex10 {
    static public void main (String[] args) {
        Scanner sc = new Scanner(System.in);

        int a, b, c;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        if (a < b && a < c) {
            System.out.println("MENOR = " + a);
        }
        else if (b < c) {
            System.out.println("MENOR = " + b);
        }
        else {
            System.out.println("MENOR = " + c);
        }
    }
}
