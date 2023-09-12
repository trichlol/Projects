/*Elabore um programa que leia elementos e os guarde dem uma matriz quadrada de ordem 3
do tipo inteiro e depois:

a) Mostre a transposta
b) Mostre a somatória dos elementos de cada linha
c) Mostre a média dos elementos da matriz*/

import java.util.Scanner;

public class Matriz {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int m[][];
        m = new int [3][];

        //Criando a Matriz
        for (int l = 0; l < m.length; l++) {
            m[l] = new int [3];

            for (int c = 0; c < 3; c++) {
                System.out.printf("Linha %d; Coluna %d: ", l, c);
                m[l][c] = sc.nextInt();
            }
            System.out.print("\n");
        }

        //Mostrando a Transposta
        for (int l = 0; l < m.length; l++) {
            for (int c = 0; c < m[l].length; c++) {
                System.out.print(m[c][l] + "\t");
            }
            System.out.println("");
        }

        System.out.println("");
        
        //Mostrando a Somatória de cada Linha
        for (int l = 0; l < m.length; l++) {
            int soma = 0;

            for (int c = 0; c < m[l].length; c++) {
                soma = soma + m[l][c];
            }

            System.out.println("Soma Linha " + l + ": " + soma);
        }

        System.out.println("");

        //Mostrando a Média da Matriz
        int soma = 0;
        int quant = 0;

        for (int l = 0; l < m.length; l++) {
            for (int c = 0; c < m[l].length; c++) {
                soma += m[l][c];
                quant = m.length * m[l].length;
            }
        }

        System.out.println("Média Matriz: " + soma/quant);

        sc.close();
    }
}