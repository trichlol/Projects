import java.util.Random;

public class Form2 {
    public static void main(String[] args) {

        int tamanho = 10;
        int[] vetor1 = new int[tamanho];
        int[] vetor2 = new int[tamanho];
        
        Random rand = new Random();

        System.out.println("Valores gerados:");

        for (int i = 0; i < tamanho; i++) {
            int valor = rand.nextInt(100); // Gera valores aleatórios de 0 a 99
            System.out.print(valor + " ");

            if (valor % 2 == 0) {
                vetor1[i] = valor;
            } else {
                vetor2[i] = valor;
            }
        }

        System.out.println("\n\nValores no vetor1:");
        for (int i = 0; i < tamanho; i++) {
            if (vetor1[i] != 0) {
                System.out.print(vetor1[i] + " ");
            }
        }

        System.out.println("\n\nValores no vetor2:");
        for (int i = 0; i < tamanho; i++) {
            if (vetor2[i] != 0) {
                System.out.print(vetor2[i] + " ");
            }
        }
    }
}