/*O cardápio de uma lanchonete é o seguinte:

Especificação          Código              Preço

Cachorro quente         100                 1,20

Bauru simples           101                 1,30

Bauru com ovo           102                 1,50

Hambúrger               103                 1,20

Cheeseburguer           104                 1,30

Refrigerante            105                 1,00

Faça um programa na Linguagem Java que leia o código do item pedido, a quantidade
e calcule o valor a ser pago por aquele lanche. Considere que a cada execução
somente será calculado um item. */

import java.util.Scanner;

public class Lanchonete {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("\nLANCHONETE\n");

        //Exibir cardápio
        System.out.println("Especificação\t\tCódigo\t\tPreço\n");
        System.out.println("Cachorro quente\t\t100\t\t1,20");
        System.out.println("Bauru simples\t\t101\t\t1,30");
        System.out.println("Bauru com ovo\t\t102\t\t1,50");
        System.out.println("Hambúger\t\t103\t\t1,20");
        System.out.println("Cheeseburguer\t\t104\t\t1,30");
        System.out.println("Refrigerante\t\t105\t\t1,00");

        String nome = "";
        double preco = 0.00;

        System.out.print("\nDigite o codigo do item: ");
        int cod = sc.nextInt();

        System.out.print("Digite a quantidade: ");
        int qntd = sc.nextInt();

        switch (cod) {
            case 100:
                nome = "Cachorro quente";
                preco = 1.20;
            break;

            case 101:
                nome = "Bauru simples";
                preco = 1.30;
            break;

            case 102:
                nome = "Bauru com ovo";
                preco = 1.50;
            break;

            case 103:
                nome = "Hambúrger";
                preco = 1.20; 
            break;
            
            case 104:
                nome = "Cheeseburguer";
                preco = 1.30;  
            break;
            
            case 105:
                nome = "Refrigerante";
                preco = 1.00;
            break;          
        }

        double total = preco * qntd;
        
        System.out.printf("\nVocê pediu %d " + nome + "\n", qntd);
        System.out.printf("Sua conta deu o total de R$%.2f\n", total);

        sc.close();
    }
}