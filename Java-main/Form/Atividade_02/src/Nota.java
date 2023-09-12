/*Faça um programa na Linguagem  Java  que leia quatros valores referentes a quatro
notas escolares de um aluno e imprimir uma mensagem dizendo que o aluno foi aprovado,
se o valor da média escolar for maior ou igual a 7. Se o aluno não foi aprovado, 
indicar uma mensagem informando esta condição. Apresentar junto das mensagens o
valor da média do aluno para qualquer condição.*/

import java.util.Scanner;

public class Nota {
    public static void main(String args []) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nMEDIA NOTA\n");

        //Criando o vetor
        float v [];
        v = new float [4];

        //Quardando as notas
        for (int i = 0; i < v.length; i++) {
            System.out.printf("Digite a %dº nota: ", i + 1);
            v[i] = sc.nextFloat();
        }

        //Calculo da Média
        float soma = 0;

        for (int i = 0; i < v.length; i++) {
            soma += v[i];
        }

        float media = soma / (v.length);

        if (media >= 7) {
            System.out.printf("\nMédia Final: %.2f\n", media);
            System.out.println("Aluno APROVADO!");
        }

        else {
            System.out.printf("\nMédia Final: %.2f\n", media);
            System.out.println("Aluno REPROVADO!");
        }

        sc.close();
    }
}