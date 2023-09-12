public class Form7 {
    // Método para calcular o fatorial de um valor inteiro
    public static int calcularFatorial(int valor) {
        int fatorial = 1;
        for (int i = 2; i <= valor; i++) {
            fatorial *= i;
        }
        return fatorial;
    }

    public static void main(String[] args) {
        int numero = 5; // Valor para calcular o fatorial
        int resultado = calcularFatorial(numero);

        System.out.println("O fatorial de " + numero + " é: " + resultado);
    }
}