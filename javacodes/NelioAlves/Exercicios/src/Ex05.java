import java.util.Scanner;

public class Ex05 {
    static public void main (String[] args) {
        Scanner sc = new Scanner(System.in);

        int funcionarioID, totalHoras;
        double valorHora,totalSalario;

        funcionarioID = sc.nextInt();
        totalHoras = sc.nextInt();
        valorHora = sc.nextDouble();
        totalSalario = valorHora * totalHoras;

        System.out.println("NUMBER = " + funcionarioID);
        System.out.printf("SALARY = %.2f%n", totalSalario);
    }
}
