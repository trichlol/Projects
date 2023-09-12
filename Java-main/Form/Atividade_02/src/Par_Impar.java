/*Faça um programa na Linguagem  Java  que efetue a leitura de um número inteiro
e apresentar uma mensagem informando se o número é par ou ímpar. */

import java.util.Scanner;

public class Par_Impar {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        System.out.println("\nPAR OU IMPAR\n");

        System.out.print("Digite um número: ");
        int n = sc.nextInt();

        if (n % 2 == 0) {
            System.out.println("\nO número é PAR");
        }

        else {
            System.out.println("\nO número é IMPAR");
        }

        sc.close();
    }
}