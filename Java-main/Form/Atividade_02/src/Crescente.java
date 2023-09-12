/*Faça um programa na Linguagem Java que leia 3 (três) valores inteiros e apresente
os 3 números em ordem crescente.*/

import java.util.Scanner;

public class Crescente {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        System.out.println("\nORDEM CRESCENTE\n");

        //Criando Vetor
        int v [];
        v = new int [3];
        
        //Preenchendo Vetor
        for (int i = 0; i < v.length; i++) {
            System.out.printf("Digite o %dº valor: ", i+1);
            v[i] = sc.nextInt();
        }

        //Organizando o Vetor
        for (int i = 0; i < v.length - 1; i++) {
            for (int j = 0; j < v.length - 1; j++) {
                if (v[j + 1] < v[j]) {
                    int aux = v[j];
                    v[j] = v[j + 1];
                    v[j +1] = aux;
                }
            }
        }

        System.out.println("");

        //Mostrando o vetor
        for (int i = 0; i < v.length; i++) {
            System.out.println(v[i]);
        }
        
        sc.close();
    }
}