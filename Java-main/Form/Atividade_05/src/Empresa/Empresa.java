/*Fazer um programa para ler os dados de um funcionário (nome, salário Bruto e
Desconto). Em seguida, mostrar os dados do funcionário (nome e salário líquido).
Em seguida, aumentar o salário do funcionário com base em uma porcentagem dada e
mostrar novamente os dados do funcionário. Use a classe projetada abaixo:
(conforme o PDF).*/

package Empresa;

import java.util.Scanner;

public class Empresa {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Funcionario f = new Funcionario();
        
        String nome;
        double salarioBruto;
        double desconto = 0;

        String op;

        System.out.println("\nFUNCIONÁRIO");

        do{
            System.out.println("\n1 - Cadastrar Funcionário");
            System.out.println("2 - Consultar Dados");
            System.out.println("3 - Salário Líquido");
            System.out.println("4 - Aumentar Salário");
            System.out.println("Q - Sair\n");
            System.out.print("Opção: ");
            op = sc.nextLine();

            switch(op){
                case "1":
                    System.out.print("\nNome: ");
                    nome = sc.nextLine();
                    System.out.print("Salário Bruto: ");
                    salarioBruto = sc.nextDouble();
                    System.out.print("Desconto: ");
                    desconto = sc.nextDouble();

                    f.cadastrar(nome, salarioBruto, desconto);
                    break;

                case "2":
                    System.out.println("\nDados do Funcionário: " + f.getNome() + ", R$" + f.getSalario());
                    break;

                case "3":
                    System.out.println("\nSalário Líquido: " + f.salarioLiquido());
                    break;

                case "4":
                    System.out.print("\nDeseja aumentar o salário em qual porcentagem? ");
                    double porcentagem = sc.nextDouble();
                    sc.nextLine();
                    f.aumentarSalario(porcentagem);
                    break;

                case "Q":
                    break;
            }

        }while(!op.equalsIgnoreCase("Q"));

        sc.close();
    }
}