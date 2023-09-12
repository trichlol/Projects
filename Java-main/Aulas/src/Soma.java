import java.util.Scanner;

public class Soma {
    public static void main (String args[]) {
        int a, b;

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o primeiro valor: ");
        a = sc.nextInt();
        System.out.print("Digite o segundo valor: ");
        b = sc.nextInt();
        System.out.print("O resultado da soma é " + (a+b));

        sc.close();
    }
}