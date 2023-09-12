/*Faça um programa na Linguagem  Java  que efetue a leitura de cinco números
inteiros e identificar o maior e o menor valor. Não execute a ordenação de
valores.*/

import java.util.Scanner;

public class MaiorMenor {
    public static void main(String[] args) {

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
        int maior = Integer.MIN_VALUE;
        int menor = Integer.MAX_VALUE;

        for (int i = 0; i < v.length; i++) {
            if (v[i] > maior) {
                maior = v[i];
            }

            if (v[i] < menor) {
                menor = v[i];
            }
        }

        System.out.println("\nO maior valor é: " + maior);
        System.out.println("O menor valor é: " + menor);

        sc.close();
    }
}