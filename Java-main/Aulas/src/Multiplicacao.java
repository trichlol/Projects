import java.util.Scanner;

public class Multiplicacao {
    public static void main(String args[]) {
        double a, b;

        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o primerio valor: ");
        a = sc.nextDouble();
        System.out.print("Digete o segundo valor: ");
        b = sc.nextDouble();

        System.out.println("O resultado da multiplicação é " + (a*b));
        System.out.printf("%f * %f = %e\n", a, b, (a*b));

        sc.close();
    }
}