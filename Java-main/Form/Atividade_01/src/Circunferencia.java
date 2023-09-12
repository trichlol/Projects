/*Faça um programa na Linguagem Java que calcule a área da circunferência. */

import java.util.Scanner;

public class Circunferencia {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nÁREA CIRCUNFERÊNCIA");

        System.out.print("\nDigite o raio da circunferencia: ");
        int raio = sc.nextInt();

        double pi = 3.14;
        double area = pi * Math.pow(raio, 2);

        System.out.println("area da circunferencia: " + area);

        sc.close();
    }
}