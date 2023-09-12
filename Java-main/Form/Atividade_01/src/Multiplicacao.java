/*Faça um programa na linguagem Java que receba 2 números e apresente a
multiplicação dos dois números.*/

import java.util.Scanner;

public class Multiplicacao {
	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		
		System.out.println("\nMULTIPLICAÇÃO");

		System.out.print("\nDigite o primeiro valor: ");
		double n1 = sc.nextDouble();

		System.out.print("Digite o segundo valor: ");
		double n2 = sc.nextDouble();
		
		double res = n1 * n2;

		System.out.println("\nO resultado é: " + res);
		sc.close();
	}
}