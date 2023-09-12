import java.util.Scanner;

public class Nome {
    public static void main(String[] args) {

        //Definição de uma nova variável
        Scanner sc = new Scanner(System.in);

        //Saída de dados
        System.out.print("Digite o seu nome: ");
        //Entrada de dados
        String nome = sc.nextLine();

        System.out.print("Digite a sua idade: ");
        int idade = sc.nextInt();

        System.out.println("\nSeja bem-vindo, " + nome);
        System.out.println("Você tem " + idade + " anos");

        sc.close();
    }
}
