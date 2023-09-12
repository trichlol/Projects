public class Booleano {
    public static void main(String[] args) {
        boolean p[] = {true, true, false, false};
        boolean q[] = {true, false, true, false};
        
        for (int i = 0; i < p.length; i++) {
            System.out.println("\nOr: " + (p[i] || (!q[i])));
            System.out.println("And: " + (p[i] && (!q[i])));
        }
    }
}