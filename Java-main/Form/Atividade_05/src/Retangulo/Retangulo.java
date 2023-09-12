package Retangulo;

public class Retangulo {
    
    private double largura;
    private double altura;

    Retangulo(double largura, double altura) {
        setAltura(altura);
        setLargura(largura);
    } 

    void area() {
        double resultado = this.largura * this.altura;
        System.out.println("AREA = " + resultado);
    }

    void perimetro() {

        double resultado = (largura * 2) + (altura * 2);
        System.out.println("PERIMETRO =  " + resultado);
    }

    void diagonal() {
        double resultado = Math. sqrt(Math.pow(largura, 2) + Math.pow(altura, 2));
        System.out.println("DIAGONAL =  " + resultado);
    }

    //LARGURA
    public void setLargura(double largura) {
        this.largura = largura;
    }
    public double getLargura() {
        return largura;
    }

    //ALTURA
    public void setAltura(double altura) {
        this.altura = altura;
    }
    public double getAltura() {
        return altura;
    }
}
