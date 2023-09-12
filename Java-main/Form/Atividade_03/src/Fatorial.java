/*Criar um vetor A do tipo inteiro de 5 elementos – Solicitar os valores para o usuário
e inserir no vetor A – Criar um vetor B do tipo inteiro – Ler o vetor A e para cada
elemento lido calcular o fatorial e gravar no B – Após de todos os elementos do vetor
A, mostrar os dois vetores*/

import java.util.Scanner;

public class Fatorial {
    public static void main(String args[]) throws Exception {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nFATORIAL\n");

        //Criando os Vetores
        int A [];
        A = new int [5];

        int B [];
        B = new int [5];
        
        //Colocando os valores
        for (int i = 0; i < A.length; i++) {
            System.out.print("Digite o " + (i + 1) + "º valor: ");
            A[i] = sc.nextInt();
        
            int aux = 1;

            //Calculo Fatorial
            for (int j = A[i]; j > 1; j--) {
                aux *= j;
            }
            
            B[i] = aux;
        }

        //Mostrando valores
        for (int i = 0; i < A.length; i++) {
            System.out.printf("\n%d! = %d", A[i], B[i]);
        }
        
        sc.close();
    }
}