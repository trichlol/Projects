public class Form8 {
    // Método para verificar se um número é primo
    public static boolean ehPrimo(int valor) {
        if (valor <= 1) {
            return false; // Números menores ou iguais a 1 não são primos
        }

        // Verificando se o número é divisível por algum inteiro de 2 até a raiz quadrada dele
        for (int i = 2; i <= Math.sqrt(valor); i++) {
            if (valor % i == 0) {
                return false; // Encontrou um divisor, não é primo
            }
        }
        return true; // Se não encontrou divisores, é primo
    }

    public static void main(String[] args) {
        int numero = 17; // Valor para verificar se é primo
        boolean resultado = ehPrimo(numero);

        if (resultado) {
            System.out.println(numero + " é um número primo.");
        } else {
            System.out.println(numero + " não é um número primo.");
        }
    }
}