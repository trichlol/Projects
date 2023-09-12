package Empresa;
public class Funcionario {

    private String nome;
    private double salarioBruto;
    private double desconto;

    void cadastrar(String nome, double salarioBruto, double desconto) {
        setNome(nome);
        setSalario(salarioBruto);
        setDesconto(desconto);
    }

    double salarioLiquido() {
        double salarioLiquido = salarioBruto - desconto;
        return salarioLiquido;
    }

    void aumentarSalario(double porcentagem) {
        salarioBruto += (salarioBruto * porcentagem) / 100;
    }

    //NOME
    void setNome(String nome) {
        this.nome = nome;
    }
    String getNome() {
        return nome;
    }

    //SALARIO
    void setSalario(double salarioBruto) {
        this.salarioBruto = salarioBruto;
    }
    double getSalario() {
        return salarioBruto;
    }

    //DESCONTO
    void setDesconto(double desconto) {
        this.desconto = desconto;
    }
    double getDesconto() {
        return desconto;
    }
}