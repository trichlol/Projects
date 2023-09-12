/*Faça um programa na Linguagem Java para efetuar o cálculo e a apresentação do
valor de uma prestação em atraso, utilizando a fórmula
PRESTAÇÃO<-- VALOR + (VALOR * (TAXA/100) * TEMPO). */

import java.util.Scanner;

public class Taxa {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nTAXA DE ATRASO");

        System.out.print("\nDigite o valor da parcela: ");
        double valor = sc.nextDouble();

        System.out.print("Digite os dias de atraso: ");
        double dias = sc.nextDouble();

        System.out.print("Digite o valor da taxa: ");
        double taxa = sc.nextDouble();

        double resultado = valor+(valor*(taxa/100)* dias);

        System.out.println("\nO valor da prestação é: " + resultado);
        
        sc.close();
    }
}