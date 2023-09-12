/*Criar uma coleção “A” na linguagem Java com 10 elementos–	Inserir os elementos de 1 a
10 na coleção – Criar uma outra coleção B que conterá o elemento da coleção A
multiplicado por 2 – Mostrar as duas coleçõesObs. Não efetuar a leitura de 10
elementos */

public class Multiplicacao {
    public static void main(String[] args) {

        System.out.println("\nMULTIPLICAÇÃO\n");
        
        int [] A = {1,2,3,4,5,6,7,8,9,10};
        int [] B = new int[A.length];

        for (int i = 0; i < A.length; i++) {
            B[i] = A[i] * 2;
            System.out.printf("%d * 2 = %d\n", A[i], B[i]);
        }
    }
}