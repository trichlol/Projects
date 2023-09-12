/*Faça um programa na Linguagem Java que leia uma temperatura em graus Fahrenheit
e apresentá-la convertida em graus Celsius. A formula de conversão é
C <-- (F - 32) * (5/9), sendo f a temperatura em Fahrenheit e C a temperatura em
Celsius. */

import java.util.Scanner;

public class Celsius {
    public static void main(String args [])  {

        Scanner sc = new Scanner(System.in);

        System.out.println("\n FAHRENHEIT -> CELSIUS");

        System.out.print("\nDigite a temperatura em graus Fahrenheit: ");
        float fahrenheit = sc.nextFloat();

        double celsius = (fahrenheit - 32) * (5.0/9.0);

        System.out.println("\nEm Celsius fica: " + celsius + "ºC");
        sc.close();
    }
}