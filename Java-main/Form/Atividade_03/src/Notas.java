/*Fazer um procedimento para receber as notas da primeira e da segunda prova de cinco
alunos. Armazenar as notas da primeira e da segunda prova em vetores distintos. Calcular
e escrever a média de cada aluno.*/

import java.util.Scanner;

public class Notas {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nMÉDIA NOTAS");
        
        float P1 [];
        P1 = new float [5];

        float P2 [];
        P2 = new float [5];

        for (int i = 0; i < 5; i++) {
            System.out.println("\nAluno " + (i + 1));
            System.out.print("Digite a nota da P1: ");
            P1[i] = sc.nextFloat();
            System.out.print("Digite a nota da P2: ");
            P2[i] = sc.nextFloat();
        }

        System.out.println("");

        for (int i = 0; i < 5; i++) {
            System.out.println("Aluno " + (i + 1) + ": " + (P1[i] + P2[i]) / 2);
        }

        sc.close();
    }
}