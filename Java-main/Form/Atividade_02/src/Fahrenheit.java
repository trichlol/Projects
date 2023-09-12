/*Faça um programa na Linguagem  Java  que apresente os valores de conversão de
graus Celsius em Fahrenheit, de 10 em 10 graus, iniciando a contagem em 10 graus
Celsius e finalizando em 100 graus Celsius. O programa deve apresentar os valores
das duas temperaturas. */

public class Fahrenheit {
    public static void main(String[] args) {

        System.out.println("\nFAHRENHEIT\n");

        double Fahrenheit = 0;
        int celsius = 10;

        for(int i = 1; i < 11; i++){
            Fahrenheit = (celsius * 9/5) + 32;

            System.out.println(celsius + " Celsius, " + Fahrenheit + " Fahrenheit");
            
            celsius += 10;
        }
    }
}