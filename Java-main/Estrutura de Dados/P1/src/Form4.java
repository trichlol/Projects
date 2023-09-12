public class Form4 {
    // Método para verificar se um número é primo

    public static void main(String[] args) {
        int numero = 17; // Valor para verificar se é primo
        boolean resultado = false;

        int valor = numero;
        
        if (valor > 1) {
        
            // Verificando se o número é divisível por algum inteiro de 2 até a raiz quadrada dele
            for (int i = 2; i <= Math.sqrt(valor); i++) {
                if (valor % i == 0) {
                    resultado = false; // Encontrou um divisor, não é primo
                }
            }
            resultado = true; // Se não encontrou divisores, é primo
        }
        

        if (resultado) {
            System.out.println(numero + " é um número primo.");
        } else {
            System.out.println(numero + " não é um número primo.");
        }
    }
}