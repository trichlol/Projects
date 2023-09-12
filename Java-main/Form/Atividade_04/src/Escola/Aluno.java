/*No exercício anterior crie 2 métodos.*/
package Escola;

public class Aluno {

    private String ra;
    private String nome;
    private String endereco;
    private String curso;

    void setCadastro(String ra, String nome, String endereco, String curso) {
        setRa(ra);
        setNome(nome);
        setEndereco(endereco);
        setCurso(curso);
    }

    void getCadastro() {
        System.out.println("\nRA: " + getRa());
        System.out.println("NOME: " + getNome());
        System.out.println("Endereço: " + getEndereco());
        System.out.println("Curso: " + getCurso());
    }

    //RA
    void setRa( String ra) {
        this.ra = ra;
    }
    String getRa() {
        return ra;
    }

    //NOME
    void setNome(String nome) {
        this.nome = nome;        
    } 
    String getNome() {
        return nome;
    }

    //ENDEREÇO
    void setEndereco(String endereco) {
        this.endereco = endereco;
    }
    String getEndereco() {
        return endereco;
    }

    //CURSO
    void setCurso(String curso) {
        this.curso = curso;
    }
    String getCurso() {
        return curso;
    }
}