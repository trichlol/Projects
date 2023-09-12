/*Implemente em Java um programa que leia dois números reais, calcule a
multiplicação entre ambos e mostre o resultado*/

import java.util.Scanner;

public class Multiplicacao {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o primeiro valor: ");
        double n1 = sc.nextDouble();
        System.out.print("Digite o segundo valor: ");
        double n2 = sc.nextDouble();

        double res = n1 * n2;

        System.out.println("\nO resultado da multiplicação é " + res);

        sc.close();
    }
}