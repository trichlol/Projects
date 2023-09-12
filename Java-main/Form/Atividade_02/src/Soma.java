/*Faça um programa na Linguagem  Java  para apresentar o total da soma obtida dos
cem primeiros números inteiros ( 1 + 2 + 3 + 4 + .... 98+ 99+ 100).*/

public class Soma {
    public static void main(String[] args) {

        System.out.println("\nSOMA DOS 100\n");

        int sum = 0;

        for (int i = 1; i <= 100; i++){
            sum += i;
        }

        System.out.println(sum);
    }
}