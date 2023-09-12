/*Fazer um programa para ler os valores da largura e altura de um retângulo. Em
seguida, mostrar a tela o valor da sua área, perímetro e diagonal. Usar uma classe
como diagrama abaixo: (conforme o PDF)*/

package Retangulo;

import java.util.Scanner;

public class Calculo {
    public static void main(String args[]) {
        
        Scanner sc = new Scanner(System.in);

        double largura;
        double altura;

        System.out.println("\nRETÂNGULO\n");

        System.out.print("Digite a largura do retangulo: ");
        largura = sc.nextDouble();
        System.out.print("Digite a altura do retangulo: ");
        altura = sc.nextDouble();

        Retangulo r = new Retangulo(largura, altura);

        System.out.println("");
        r.area();
        r.perimetro();
        r.diagonal();

        sc.close();
    }
}