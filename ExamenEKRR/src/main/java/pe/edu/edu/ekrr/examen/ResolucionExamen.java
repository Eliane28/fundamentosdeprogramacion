package pe.edu.edu.ekrr.examen;

import java.util.concurrent.RecursiveAction;

import pe.edu.edu.ekrr.utils.LeerTeclado;

public class ResolucionExamen {

    public static LeerTeclado teclado = new LeerTeclado();

    public void ejercicio1() {
        int cantAutomotriz = 0, costo = 0, categoria = 0, categoria1 = 0, categoria2 = 0, categoria3 = 0;
        double impuesto = 0, impuestoTotal = 0;
        System.out.println("cantidad de autos que tiene");
        cantAutomotriz = teclado.lectora(0);
        for (int i = 1; i <= cantAutomotriz; i++) {
            System.out.println("Que categoria tiene tu auto");
            categoria = teclado.lectora(0);
            System.out.println("Cuanto es el costo del carro");
            costo = teclado.lectora(0);
            if (categoria == 1) {
                impuesto = costo * 0.1;
                categoria1 = (int) (categoria1 + impuesto);
            }

            if (categoria == 2) {
                impuesto = costo * 0.7;
                categoria2 = (int) (categoria2 + impuesto);
            }

            if (categoria == 3) {
                impuesto = costo * 0.7;
                categoria3 = (int) (categoria3 + impuesto);
            }
            impuestoTotal = impuestoTotal + impuesto;
            System.out.println("el valor del impuesto:" + impuesto);
            System.out.println("");

        }
        System.out.println("valor de categoria1:" + categoria1);
        System.out.println("valor de categoria2:" + categoria2);
        System.out.println("valor de categoria3:" + categoria3);
        System.out.println(" Impuesto Total: " + impuestoTotal);
    }

    public void ejercicio2() {
        int numllegada, numpartida, multiplicado;
        System.out.println("Digite su numero de partida");
        numpartida = teclado.lectora(0);
        System.out.println("Digite el valor de llegada");
        numllegada = teclado.lectora(0);
        for (int i = numpartida; i < numllegada; i++) {
            for (int j = 0; j <= 12; j++) {
                multiplicado = i * j;
                System.out.println(i + "x" + j + "=" + multiplicado);

            }
        }
    }

    public void ejercicio3() {
        int i = 1, r, a = 0;
        System.out.println("Escribe un numero");
        r = teclado.lectora(0);
        while (i < r) {
            if (r % i == 0) {
                a = a + i;
            }
            i++;
        }
        if (a == r) {
            System.out.println("perfecto");

        } else {
            System.out.println("no perfecto");

        }
    }

    public int ejercicio4(int n, int a) {
        if (a <= 0) {
            return 1;

        } else {
            return n * ejercicio4(n, a - 1);
        }

    }
}