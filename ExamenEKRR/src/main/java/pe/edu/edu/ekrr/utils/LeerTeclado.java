package pe.edu.edu.ekrr.utils;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class LeerTeclado {
    public static BufferedReader lector = new BufferedReader(new InputStreamReader(System.in));

    public static String lectora(String dato) {
        try {
            dato = lector.readLine();
        } catch (Exception e) {
            System.err.println("ERROR string" + e.getMessage());
        }
        return dato;
    }

    public static int lectora(int dato) {
        try {
            dato = Integer.parseInt(lector.readLine());
        } catch (Exception e) {
            System.err.println("ERROR int" + e.getMessage());
        }
        return dato;
    }
    
    public static double lectora(double dato) {
        try {
            dato = Double.parseDouble(lector.readLine());
        } catch (Exception e) {
            System.err.println("ERROR double" + e.getMessage());
        }
        return dato;
    }
    
    public static float lectora(float dato) {
        try {
            dato = Float.parseFloat(lector.readLine());
        } catch (Exception e) {
            System.err.println("ERROR float" + e.getMessage());
        }
        return dato;
    }
    
    public static boolean lectora(boolean dato) {
        try {
            dato = Boolean.parseBoolean(lector.readLine());
        } catch (Exception e) {
            System.err.println("ERROR boolean" + e.getMessage());
        }
        return dato;
    }
}
