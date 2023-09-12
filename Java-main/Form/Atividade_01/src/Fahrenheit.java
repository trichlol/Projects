/*Faça um programa na Linguagem Java que leia uma temperatura em graus Celsius
e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é
F <-- (9 * C + 160) /5, sendo F a temperatura em Fahrenheit e C a temperatura
em Celsius. */

import java.util.Scanner;

public class Fahrenheit {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nCELCIUS -> FAHRENHEIT");

        System.out.print("\nDigite a temperatura em graus Celsius: ");
        float celsius = sc.nextFloat();

        float fahrenheit = (9 * celsius + 160) /5;

        System.out.println("\nEm Fahrenheit fica: " + fahrenheit + "ºF");
        sc.close();
    }
}