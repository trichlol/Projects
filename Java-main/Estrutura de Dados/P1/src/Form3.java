import java.util.Scanner;

public class Form3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            System.out.println("Menu:");
            System.out.println("1 - Somar dois números reais");
            System.out.println("2 - Subtrair dois números inteiros");
            System.out.println("3 - Exibir a tabuada de um número");
            System.out.println("4 - Sair");
            System.out.print("Escolha uma opção: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Digite o primeiro número real: ");
                    double num1 = scanner.nextDouble();
                    System.out.print("Digite o segundo número real: ");
                    double num2 = scanner.nextDouble();
                    double sum = num1 + num2;
                    System.out.println("A soma é: " + sum);
                    break;
                case 2:
                    System.out.print("Digite o primeiro número inteiro: ");
                    int int1 = scanner.nextInt();
                    System.out.print("Digite o segundo número inteiro: ");
                    int int2 = scanner.nextInt();
                    int diff = int1 - int2;
                    System.out.println("A diferença é: " + diff);
                    break;
                case 3:
                    System.out.print("Digite um número para exibir a tabuada: ");
                    int num = scanner.nextInt();
                    System.out.println("Tabuada do " + num + ":");
                    for (int i = 1; i <= 10; i++) {
                        System.out.println(num + " * " + i + " = " + (num * i));
                    }
                    break;
                case 4:
                    System.out.println("Saindo do programa.");
                    break;
                default:
                    System.out.println("Opção inválida. Escolha novamente.");
            }
        } while (choice != 4);

        scanner.close();
    }
}