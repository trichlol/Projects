/*Faça um programa na linguaguem Java para calcular e apresentar o valor do
volume de uma lata de óleo, utilizando a fórmula: VOLUME <-- 3.14159 *
RAIO2 * ALTURA. */

import java.util.Scanner;

public class Volume {
    public static void main(String args[]) {
        
        Scanner sc = new Scanner(System.in);

        System.out.println("\nVOLUME");

        double pi = 3.14159;

        System.out.print("\nDigite o raio da lata: ");
        double raio = sc.nextDouble();

        System.out.print("Digite a altura da lata: ");
        double altura = sc.nextDouble();

        double volume = pi * Math.pow(raio, 2)* altura;

        System.out.println("O volume da lata é de " + volume + "m³");
        sc.close();
    }
}