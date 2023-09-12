/*Faça um programa na Linguagem Java que que receba um número e mostre o
fatorial desse número.*/

import java.util.Scanner;

public class Fatorial {
    public static void main(String args []) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nFATORIAL\n");

        System.out.print("Digite um número: ");
        int num = sc.nextInt();

        int n = num;
        int aux = 1;

        while (n >= 2) {
            aux *= n;
            n -= 1;
        }

        System.out.println("\n" + num + "! = " + aux);

        sc.close();
    }
}