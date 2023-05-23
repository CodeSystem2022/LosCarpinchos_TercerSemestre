package domain;

public enum TipoEscrituras {
    CLASICO ("Escritura a mano"),
    MODERNO ("Escritura digital");
    
    private final String descripcion;
    // CONSTRUCTOR
    private TipoEscrituras(String descripcion) {
        this.descripcion = descripcion;
    }
    // METODO GET
    public String getDescripcion() {
        return this.descripcion;
    }
}