public class Form6 {
    
    public static void main(String[] args) {
        int numero = 5; // Valor para calcular o fatorial
        int valor = numero;
        int fatorial = 1;
        for (int i = 2; i <= valor; i++) {
            fatorial *= i;
        }

        System.out.println("O fatorial de " + numero + " é: " + fatorial);
    }
}