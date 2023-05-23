// CLASE HIJA
package domain;

public class Escritor extends Empleado {
    final TipoEscrituras tipoEscrituras;
    // CONSTRUCTOR
    public Escritor(String nombre, double sueldo, TipoEscrituras tipoEscrituras1){
        super(nombre, sueldo);
        this.tipoEscrituras = tipoEscrituras1;
    }
    // METODO PARA SOBREESCRIBIR
    @Override
    public String obtenerDetalles() {
        return super.obtenerDetalles() + ", Tipo Escritura: " +
                tipoEscrituras.getDescripcion();
    }
    
    @Override
    public String toString() {
        return "Escritor{" + "tipoEscrituras: " + tipoEscrituras + '{' +
                "" + super.toString();
    }
    
    public TipoEscrituras geTipoEscrituras() {
        return this.tipoEscrituras;
    }
}
