/*Faça um programa na Linguagem Java para efetuar a leitura de um número inteiro
e apresentar o resultado do quadrado desse número. */

import java.util.Scanner;

public class Elevar {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nELEVAR AO QUADRADO");

        System.out.print("\nDigite um número: ");
        int numero = sc.nextInt();

        System.out.println("\nO quadrado desse número é " + Math.pow(numero, 2));
        
        sc.close();
    }
}