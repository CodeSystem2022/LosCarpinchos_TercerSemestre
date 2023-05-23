package test;

import domain.*;

public class TestClaseObject {
    public static void main(String[] args) {
        // comparacion de 2 objetos de la CLASE EMPLEADO
        Empleado empleado1 = new Empleado("Juan", 5000.0); 
        Empleado empleado2 = new Empleado("Guss", 5000.0);
        
        if (empleado1 == empleado2) {
            System.out.println("Tiene la misma referencia de memoria");
        }
        else {
            System.out.println("Tienen distinta referencia de memoria");
        // RESULTADO
        // Tienen distinta referencia de memoria
        }
        // Equals()
        // El método equals() compara dos cadenas y devuelve verdadero si las 
        // cadenas son iguales y falso en caso contrario. Sugerencia: use el
        // método compareTo() para comparar dos cadenas lexicográficamente.
        if (empleado1.equals(empleado2)) {
            System.out.println("Los objetos son iguales en contenido");
        // RESULTADO
        // Los objetos son distintos en contenido
        }        
        else {
            System.out.println("Los objetos son distintos en contenido");
        }
        // HashCode
        // El método hashCode() se utiliza para generar los valores hash de 
        // los objetos. Usando estos valores hash, estos objetos se almacenan en colecciones
        if (empleado1.hashCode() == empleado2.hashCode()) {
            System.out.println("El valor hashCode es igual");
        }       
        else {
            System.out.println("El valor hashCode es diferente");
        // RESULTADO
        // El valor hashCode es diferente
        }
    }    
}