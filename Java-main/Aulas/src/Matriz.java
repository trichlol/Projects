import java.util.Scanner;

public class Matriz {
    public static void main(String [] args) {

        Scanner sc = new Scanner(System.in);

        //Criando a Matriz
        int m[][];
        m = new int[3][];

        //Preenchendo a Matriz
        for (int l = 0; l < m.length; l++) {
            m[l] = new int [3];

            for (int c = 0; c < m[l].length; c++) {
                System.out.printf("Linha %d; Coluna %d: ", l, c);
                m[l][c] = sc.nextInt();
            }
            System.out.print("\n");
        }

        //Mostrando a Matriz
        for(int l = 0; l < m.length; l++) {
            for(int c = 0; c < m[l].length; c++) {
                System.out.print(m[l][c] + "\t");
            }
            System.out.print("\n");
        }

        sc.close();
    }
}