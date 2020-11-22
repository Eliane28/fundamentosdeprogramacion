package pe.edu.edu.ekrr.examen;

import pe.edu.edu.ekrr.utils.LeerTeclado;

public class ResolucionExamen {
    
    public static LeerTeclado teclado = new LeerTeclado();
    
    public void ejercicio1() {

    }

    public void ejercicio2() {
        int numllegada, numpartida, multiplicado;
        System.out.println("Digite su numero de partida");
        numpartida=teclado.lectora(0);
        System.out.println("Digite el valor de llegada");
        numllegada=teclado.lectora(0);
        for (int i = numpartida; i < numllegada; i++) {
            for (int j = 0; j <= 12; j++) {
                multiplicado = i * j;
                System.out.println(i + "x"+j+"="+ multiplicado);
                
            }
        }
    }

    public void ejercicio3() {

    }

    public void ejercicio4() {

    }
}