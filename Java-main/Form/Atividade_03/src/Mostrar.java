/*Criar uma coleção na linguagem Java com 10 elementos–	Inserir os elementos de 1 a 10
no vetor – Após a inserção, somente após a inserção mostrar o vetor. Obs: Não efetuar
a leitura de 10 elementos*/

public class Mostrar {
    public static void main(String[] args) {

        System.out.println("\nVETOR\n");

        int[] v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  
        for (int i = 0; i < v.length; i++) {
            System.out.printf("[%d] ", v[i]);
        }
    }
}