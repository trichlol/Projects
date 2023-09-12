public class Form5 {
    public static void main (String args[]){
      
      String entra = "2023";
      int leds=0;
      char car=' ';
      for (int i=0; i<entra.length();i++){
          car = entra.charAt(i);
          if (car == '0' || car == '6' || car == '9')
             leds = 6;
          else
            if (car == '1')
               leds = 2;
            else
               if (car == '7')
                  leds = 3;
               else
                   if (car == '4')
                      leds = 4;
                   else
                        if (car == '2' || car == '3' || car == '5')
                           leds = 5;
                        else
                           if (car == '8')
                              leds = 7;
                           else
                              leds = 0;
          
          if (leds != 0)
            System.out.printf("Dígito %s acende %d leds\n",car,leds);
          else 
            System.out.printf("Sequencia incorreta de dígitos");
     }
  }
}