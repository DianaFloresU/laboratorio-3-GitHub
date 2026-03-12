package Prog1018;
import java.util.Scanner;
public class Prog1018 {
public static void main(String[] args) {
        Scanner leer =new Scanner (System.in);
        int a,b,c;
        a=0;b=0;c=0;
        a=leer.nextInt();
        for (int i=1;i<=a;i++)
        {
            b=leer.nextInt(); c=leer.nextInt();
            if(b<c)
            {
                System.out.println("<");
            }
            if(b>c)
            {
                System.out.println(">");
            }
            if (b==c)
            {
                System.out.println("=");
            }
        }       
    } 
}
