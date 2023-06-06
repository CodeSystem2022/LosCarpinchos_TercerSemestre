// let persona3= new Persona('asdf','asdf'); no se puede antes de la creación

class Persona{
	static contadorPersona = 0;

	static get MAX_OBJ(){
		return 5;
	}

	//email = 'Valor default email';//no estático

		constructor(nombre, apellido){
			this._nombre = nombre;
		    this._apellido = apellido;
			if(Persona.contadorPersona < Persona.MAX_OBJ){
				this.idPersona = ++Persona.contadorPersona;
			}else{
				console.log('Se ha superado el numero máximo de objetos');
				
			}			
			
	}
	get nombre(){
		return this._nombre;
	}
	set nombre(nombre){
		this._nombre = nombre;
	}

	get apellido(){
		return this._apellido;
	}
	set apellido(apellido){
		this._apellido = apellido;
	}
	nombreCompleto(){
		return this.idPersona+' '+this._nombre+' '+this.apellido;
	}
	toString(){
		return this.nombreCompleto();
	}
	static saludar(){
		console.log('Saludos desde este método static');
	}
	static saludar2(persona){
		console.log(persona.nombre+' '+persona.apellido);
	}
}

class Empleado extends Persona{//hija	

	constructor(nombre,apellido,departamento){
		super(nombre,apellido);
		this._departamento=departamento;
	}
	get departamento(){
		return this._departamento;
	}
	set departamento(departamento){
		this._departamento =departamento;
	}

	//sobreescribir metodo
	nombreCompleto(){
		return super.nombreCompleto()+', '+this._departamento;
	}
}



let persona1 = new Persona('Martín', 'Perez');
console.log(persona1.nombre);
persona1.nombre = "Juan Carlos";
console.log(persona1.nombre);


let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = "Maria Laura";
console.log(persona2.nombre);

let empleado1 = new Empleado('Javier','Portal','Ventas');

console.log(empleado1);
console.log(empleado1.nombreCompleto());

console.log(empleado1.toString());

console.log(persona1.toString());

Persona.saludar();

Persona.saludar2(persona1);

Persona.saludar2(empleado1);

console.log(Persona.contadorPersona);
console.log(Empleado.contadorPersona)

console.log(persona1.email);
console.log(empleado1.email);
//console.log(Persona.email); no se puede, se asocia solo a las instancias y no a la clase

console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());

console.log(Persona.contadorPersona);

let persona3 = new Persona('Carlita','Bertosi');
console.log(persona3.toString());
console.log(Persona.contadorPersona);

console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ=10; //no se puede modificar
console.log(Persona.MAX_OBJ);

let persona4 = new Persona('Franco','Diaz');
console.log(persona4.toString());
let persona5 = new Persona('Liliana', 'Paz');
console.log(persona5.toString());