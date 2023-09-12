/*Faça um programa na Linguagem  Java  que leia 3 números inteiros e mostre o
maior deles.*/

import java.util.Scanner;

public class Maior {
    public static void main(String args[]) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nMAIOR VALOR\n");

        //Criando o Vetor
        int v [];
        v = new int [3];

        //Lendo os valores
        for (int i = 0; i < v.length; i++) {
            System.out.printf("Digite o %dº valor: ", i + 1);
            v[i] = sc.nextInt();
        }

        //Maior valor
        int maior = 0;
        for (int i = 0; i < v.length; i++) {
            if (v[i] > maior) {
                maior = v[i];
            }
        }

        System.out.println("\nO maior valor é: " + maior);

        sc.close();
    }
}