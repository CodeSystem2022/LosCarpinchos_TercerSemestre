//let persona3 = new Persona('Carla', 'Ponce');

class Persona {

    constructor(nombre, apellido) {

        this._nombre = nombre;
        this._apellido = apellido;

    }
    get nombre() {

        return this._nombre;
    }

    set nombre(nombre) {

        this._nombre = nombre;

    }
}
class Empleado extends Persona
{
    constructor(departamento) // clase hija
    {
        super(nombre, apellido);
    this._departamento = departamento;
    }


    get departamento() {

        return this._departamento;
    }

    set departamento(departamento) {

        this._departamento = this.departamento;

    }

}

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);

let persona2 = new Persona('Carlos', 'Lara');

console.log(persona2.nombre);

persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');

console.log(empleado1);
console.log(empleado1.nombre);