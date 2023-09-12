/*Faça um programa na Linguagem Java que leia a idade de uma pessoa expressa em
ano, mês e dia e mostre-as em dias. */

import java.util.Scanner;

public class Idade {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nCONVERSOR DE ANOS");

        System.out.print("\nDigite sua idade: ");
        int anos = sc.nextInt();

        System.out.print("Quantidade de meses que já se passaram do seu aniversário: ");
        int meses = sc.nextInt();

        System.out.print("Quantidade de dias que já se passaram do seu aniversário: ");
        int dias = sc.nextInt();

        dias = (anos * 360) + (meses * 30) + dias;

        System.out.println("\nParabéns! Você já viveu por " + dias + " dias");
        sc.close();
    }
}