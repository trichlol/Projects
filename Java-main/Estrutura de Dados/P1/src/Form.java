import java.util.Random;

public class Form {
    public static void main(String[] args) {

        int[][] matrizOriginal = new int[4][4];
        int[][] matrizNova = new int[4][4];
        
        Random rand = new Random();

        // Preenchendo a matriz com valores aleatórios de 1 a 100
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                matrizOriginal[i][j] = rand.nextInt(100) + 1;
            }
        }

        System.out.println("Matriz Original:");

        // Imprimindo a matriz original
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                System.out.print(matrizOriginal[i][j] + "\t");
            }
            System.out.println();
        }

        //Preenchendo a nova matriz
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                matrizNova[i][j] = (matrizOriginal[i][j] % 2 == 0) ? 0 : 1;
            }
        }

        System.out.println("\nMatriz Nova:");

        // Imprimindo a nova matriz 
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                System.out.print(matrizNova[i][j] + "\t");
            }
            System.out.println();
        }
    }
}