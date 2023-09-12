/*Implemente em Java um programa que leia dois números inteiros e mostre a soma*/

import java.util.Scanner;

public class Soma {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o primeiro valor: ");
        int n1 = sc.nextInt();
        System.out.print("Digite o segundo valor: ");
        int n2 = sc.nextInt();

        int res = n1 + n2;
        System.out.println("\nO resultado da soma é: " + res);

        sc.close();
    }
}