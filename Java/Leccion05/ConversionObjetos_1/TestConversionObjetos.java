
package test;

import domain.*;

public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado; // Variable de la CLASE PADRE
        // ASIGNAMOS REFERNCIA A LA VARIABLE
        empleado = new Escritor("Juan", 5000, TipoEscrituras.CLASICO);
        //System.out.println("empleado = " + empleado);
// RESULTADO
// empleado = Escritor{tipoEscrituras=CLASICO} Empleado{nombre=Juan, sueldo=5000.0}

        // SI QUEREMOS ACCEDER A METODOS ESCRITOR
        System.out.println(empleado.obtenerDetalles());
// RESULTADO
// Nombre: Juan, Sueldo: 5000.0, Tipo Escritura: Escritura a mano
        
        // DOWNCASTING
        // Se convierte una CLASE PADRE a una CLASE HIJA
        // TENEMOS DOS OPCIONES, ESTA ES UNA
        //((Escritor)empleado).getTipoEscrituras();
        Escritor escritor = (Escritor)empleado; // Esta es la segunda opcion
        escritor.geTipoEscrituras();
        
        // UPCASTING
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
// RESULTADO
// Nombre: Juan, Sueldo: 5000.0, Tipo Escritura: Escritura a mano
    }
}
