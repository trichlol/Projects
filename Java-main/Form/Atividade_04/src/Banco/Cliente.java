/*No exercício anterior crie 2 métodos.*/

package Banco;

public class Cliente {
    
    private String conta;
    private String nome;
    private String cpf;
    private float saldo = 0f;

    void setCadastro(String conta, String nome, String cpf) {
        setConta(conta);
        setNome(nome);
        setCPF(cpf);
    }

    void getCadastro() {
        System.out.println("\nCONTA: " + getConta());
        System.out.println("NOME: " + getNome());
        System.out.println("CPF: " + getCPF());
    }

    void depositar(float saldo) {
        this.saldo += saldo;
    }

    void sacar(float saldo) {
        if (saldo > this.saldo){
            System.out.println("Você não possui esse valor em sua conta");
        }
        else {
            this.saldo -= saldo;
        }
    }

    //CONTA
    void setConta(String conta) {
        this.conta = conta;
    }
    String getConta() {
        return conta;
    }

    //NOME
    void setNome(String nome) {
        this.nome = nome;
    }
    String getNome() {
        return nome;
    }

    //CPF
    void setCPF(String cpf) {
        this.cpf = cpf;
    }
    String getCPF() {
        return cpf;
    }

    //SALDO
    void setSaldo(float saldo) {
        this.saldo = saldo;
    }
    float getSaldo() {
        return saldo;
    }
}