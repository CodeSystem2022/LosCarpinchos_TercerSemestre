
package ar.com.system2023.mundopc;

public class Teclado extends DispositivoEntrada{
    //agregamos atributos para esta clase hija
    private final int idTeclado;
    private static int contadorTeclados;
    
    public Teclado(String tipoEntrada, String marca){
        super(tipoEntrada, marca);
        this.idTeclado = ++Teclado.contadorTeclados;   
    }

    @Override
    public String toString() {
        return "Teclado{" + "idTeclado=" + idTeclado +", "+super.toString() +'}';
    }
    
}
