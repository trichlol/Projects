/*Faça um programa na Linguagem Java que efetue a apresentação do valor da
conversão em real de um valor lido em dólar. O programa deve solicitar o valor
da cotação do dólar e também a quantidade de dólares disponível com o usuário,
para que seja apresentado o valor em moeda brasileira. */

import java.util.Scanner;

public class Dolar {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nCOTAÇÃO DO DOLAR");

        System.out.print("\nDigite a cotação atual do dolar: ");
        double cotacao = sc.nextDouble();

        System.out.print("Quantidade de Dólares disponível: ");
        double dolares = sc.nextDouble();

        System.out.printf("\nVocê tem R$%.2f\n", dolares * cotacao);

        sc.close();
    }
}