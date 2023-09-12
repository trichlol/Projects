/*Fazer um programa para ler os dados de uma conta corrente:

- Número da Conta;
- Nome do Cliente;
- CPF;
- Saldo Da conta.

Em seguida, mostrar a tela todos os atributos. Utilize classe.*/

package Banco;

import java.util.Scanner;

public class ContaCorrente {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        Cliente c = new Cliente();

        String conta;
        String nome;
        String cpf;
        float saldo;

        String op = "";

        System.out.println("\nCONTA CORRENTE");

        while (!op.equalsIgnoreCase("Q")) {
            System.out.println("\nDigite a opção que deseja realizar:");
            System.out.println("");
            System.out.println("1 - Realizar cadastro");
            System.out.println("2 - Mostrar dados");
            System.out.println("3 - Mostrar saldo atual");
            System.out.println("4 - Fazer depósito");
            System.out.println("5 - Realizar saque");
            System.out.println("Q - Sair do programa\n");

            System.out.print("OPÇÃO: ");
            op = sc.nextLine();
            
            //REALIZAR CADASTRO
            if (op.equals("1")){
                System.out.print("\nDigite o número da sua conta: ");
                conta = sc.nextLine();
                System.out.print("Digite o seu nome: ");
                nome = sc.nextLine();
                System.out.print("Digite o seu CPF: ");
                cpf = sc.nextLine();

                c.setCadastro(conta, nome, cpf);
            }

            //MOSTRAR DADOS
            else if (op.equals("2")) {
                c.getCadastro();
            }

            //MOSTRAR SALDO
            else if(op.equals("3")) {
                System.out.printf("\nSALDO ATUAL: %.2f\n", c.getSaldo());
            }

            //FAZER DEPÓSITO
            else if(op.equals("4")) {
                System.out.print("\nValor do depósito: ");
                saldo = sc.nextFloat();
                c.depositar(saldo);
            }

            //REALIZAR SAQUE
            else if(op.equals("5")) {
                System.out.print("\nValor do saque: ");
                saldo = sc.nextFloat();
                c.sacar(saldo);
            }

            else if (op.equalsIgnoreCase("Q")) {
                System.out.println("\nFinalizando o sistema");
            }

            else {
                System.out.println("\nOpção não correspondente!");
            }
        }

        sc.close();
    }
}