import java.util.Scanner;

public class Ex08 {
    static public void main (String[] args) {
        Scanner sc = new Scanner(System.in);

        String aluno;
        double nota1, nota2, media;
        System.out.println("Qual o nome do aluno?");
        aluno = sc.next();

        System.out.println("Digite a primeira nota de " + aluno);
        nota1 = sc.nextDouble();

        System.out.println("Agora digite segunda nota de " + aluno);
        nota2 = sc.nextDouble();

        media = nota1 + nota2;

        if (media < 60.0) {
            System.out.printf("Nota final = %.1f%n", media);
            System.out.println("REPROVADO!");
        }
        else {
            System.out.printf("Nota final = %.1f%n", media);
            System.out.println("APROVADO!");
        }
    }
}
