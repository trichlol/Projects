/*Faça um programa na Linguagem Java que receba um número e mostre o resto
da divisão por 6. */

import java.util.Scanner;

public class Resto {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nRESTO DE 6");

        System.out.print("\nDigite um numero: ");
        int numero = sc.nextInt();

        System.out.println("\nO resto da divisão de " + numero +" por 6 é " + numero % 6);

        sc.close();
    }
}