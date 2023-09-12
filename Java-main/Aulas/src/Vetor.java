import java.util.Scanner;

public class Vetor {
    public static void main(String args[]) {
        
        Scanner sc = new Scanner(System.in);

        String nome[] = new String[3];
        int idade[] = new int[3];
        double estatura[] = new double[3];
        double peso[] = new double[3];
        double imc[] = new double[3];
        
        for(int i = 0; i < 3; i++){
            System.out.print("Digite o nome da "+(i+1)+"° pessoa: ");
            nome[i] = sc.nextLine();

            System.out.print("Digite a idade da "+(i+1)+"° pessoa: ");
            idade[i] = sc.nextInt();

            System.out.print("Digite a estatura da "+(i+1)+"° pessoa: ");
            estatura[i] = sc.nextDouble();

            System.out.print("Digite o peso da "+(i+1)+"° pessoa: ");
            peso[i] = sc.nextDouble();

            imc[i] = peso[i] % (estatura[i] * estatura[i]);

            System.out.println("");
        }
        
        for(int i = 0; i < 3; i++){
            System.out.println("\nDados da " + (i+1) + "° pessoa:\nNome:" + nome[i] + "\nIdade:" + idade[i] + "\nEstatura:"+estatura[i] + "\nPeso:" + peso[i] + "\nIMC:" + imc[i]);
        }
        
        sc.close();
    }
}