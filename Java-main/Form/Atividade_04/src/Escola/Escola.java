/*Fazer um programa para ler os dados de um Aluno:

- RA;
- Nome;
- Endereço;
- Curso.

Em seguida, mostrar a tela todos os atributos. Utilize classe.*/


package Escola;

import java.util.Scanner;

public class Escola {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        Aluno a = new Aluno();

        String ra;
        String nome;
        String endereco;
        String curso;

        String op = "";

        System.out.println("\nPROGRAMA ESCOLAR");

        while (!op.equalsIgnoreCase("Q")) {
            System.out.println("\nDigite a opção que deseja realizar:");
            System.out.println("");
            System.out.println("1 - Cadastrar");
            System.out.println("2 - Mostrar informações");
            System.out.println("Q - Sair do programa\n");

            System.out.print("OPÇÃO: ");
            op = sc.nextLine();

            if (op.equals("1")) {
                System.out.print("\nDigite o seu RA: ");
                ra = sc.nextLine();
                System.out.print("Digite o seu nome: ");
                nome = sc.nextLine();
                System.out.print("Digite o seu endereço: ");
                endereco = sc.nextLine();
                System.out.print("Digite o seu curso: ");
                curso = sc.nextLine();

                a.setCadastro(ra, nome, endereco, curso);
            }

            else if (op.equals("2")) {
                a.getCadastro();
            }

            else if (op.equalsIgnoreCase("Q")) {
                System.out.println("\nEncerrando programa.");
            }

            else {
                System.out.println("\nOpção não correspondente!");
            }
        }

        sc.close();
    }
}