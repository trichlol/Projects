/*Faça um programa na Linguagem Java  para ler dois valores inteiros para as
variáveis A e B e efetuar a troca dos valores de forma que a variável A passe
a possuir o valor da variável B e a variável B passe a possuir o valor da
variável A. Apresentar os valores trocados. */

import java.util.Scanner;

public class Troca {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nTROCA DE VARIÁVEIS");

        System.out.print("\nDigite o valor de A: ");
        int a = sc.nextInt();

        System.out.print("Digite o valor de B: ");
        int b = sc.nextInt();

        int aux = b;
        b = a;
        a = aux;

        System.out.println("\nValor de A: " + a);
        System.out.println("Valor de B: " + b);
        
        sc.close();
    }
}