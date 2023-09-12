public class ListaDeInteiros {
    private int dados[];
    private int tamanho;
 
    public ListaDeInteiros(int capMax){
        dados = new int[capMax];
        //o java pré inicializa os atributos do tipo inteiro
        //com o valor 0 (zero), do tipo real com o 
        //valor 0.0(zero ponto zero) e atributos com tipo
        //abstrato de dados são inicializados com null
        //Portanto tamanho recebeu o valor 0(zero)
        
    }

    //Inclua este método na classe ListaDeInteiros
    public void adicionaFinal (int e)throws Exception{
        if (dados.length != tamanho) {
        // não está cheia
        dados[tamanho] = e;
        tamanho = tamanho + 1;
        } else {
            //sim está cheia
            throw new Exception("ERRO! Lista Cheia");
        }
    }

    public String toString() {
        String s = "\nElementos: ";
        for (int i = 0; i < tamanho; i++) {
            s = s + " " + dados[i];
        }

        s = s + "\nTamanho: " + tamanho;
        return s;
    }

    public int removeFinal ( ) throws Exception {
        if (tamanho != 0) {
            // não está vazia
            tamanho = tamanho - 1;
            return dados[tamanho] ;
        } else {
            //sim está vazia
            throw new Exception("ERRO! Lista Vazia");
        }
    }
}

