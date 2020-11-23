package pe.edu.edu.ekrr;

import pe.edu.edu.ekrr.examen.ResolucionExamen;
import pe.edu.edu.ekrr.utils.LeerTeclado;

public class App 
{
    public static void main( String[] args )
    {
        ResolucionExamen examen= new ResolucionExamen();
        int n, e;
        System.out.println("Dame el numero base: ");
        n = teclado.lectora(0);
        System.out.println("Dame un numero exponencial: ");
        e = teclado.lectora(0);

        System.out.println(examen.ejercicio4(n, e));
    }
    public static LeerTeclado teclado=new LeerTeclado();
}
