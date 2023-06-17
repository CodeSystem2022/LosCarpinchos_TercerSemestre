class Cliente extends Persona {

    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fechaRegistro) {
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = fechaRegistro;
    }

    get idCliente() {
        return this._idCliente;
    }

    get fechaRegistro() {
        this._fechaRegistro;
    }

    set fecharegistro(sueldo) {
        this._fechaRegistro = fecharegistro;
    }

    toString() {
        return `
        ${super.toString()} 
        ${this._idCliente} 
        ${this._fechaRegistro}`;
    }
}