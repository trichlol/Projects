import java.util.Scanner;

public class Grafo {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        //Criando a Matriz vazia
        int m [][];
        m = new int[3][];

        for (int l = 0; l < m.length; l++) {
            m [l] = new int [3];
            for (int c = 0; c < m[l].length; c++) {
                m [l][c] = -1;
            }
        }

        //Exibindo o Grafo1
        System.out.println("\nGRAFO ATUAL\n");

        System.out.println("X\t0\t1\t2");

        for (int l = 0; l < m.length; l++) {
            System.out.print(l + "\t");

            for (int c = 0; c < m[l].length; c++) {
                System.out.print(m[l][c] + "\t");
            }

            System.out.println();
        }

        int origem = 0;
        int destino = 0;

        int opcao = 0;
        
        while (m[origem][destino] <= 1) {

            System.out.println("\nEscolha a ação desejada:");
            System.out.println("");
            System.out.println("1 - ADICIONAR ARESTA");
            System.out.println("2 - MOSTRAR GRAFO");
            System.out.println("");
            System.out.print("OPÇÃO: ");
            opcao = sc.nextInt();

            if (opcao == 1) {
                //Inserindo Origem e Destino
                System.out.print("\nInsira a origem: ");
                origem = sc.nextInt();

                System.out.print("Insira o destino: ");
                destino = sc.nextInt();

                for (int l = 0; l < m.length; l++) {
                    for (int c = 0; c < m[l].length; c++) {
                        if (l == origem && c == destino) {
                            m[l][c] += 2;
                        }
                    }
                }
            }

            else if (opcao == 2) {
                //Exibindo novo Grafo
                System.out.println("\nGRAFO ATUAL\n");

                System.out.println("X\t 0\t 1\t 2");

                for (int l = 0; l < m.length; l++) {
                    System.out.print(l + "\t");

                    for (int c = 0; c < m[l].length; c++) {
                        System.out.print(m[l][c] + "\t");
                    }

                    System.out.println();
                }
            }
        }

        sc.close();
    }
}
