let x = 10; //variable de tipo primitiva

console.log(x.length); 




console.log('   Tipos primitivos'); 


//Objeto

let persona = {

    nombre: 'Carlos',

    apellido: 'Gil',

    email: 'cgil@gmail.com',

    edad: 30,

    nombreCompleto: function() { //método o función en JavaScript 
        return this.nombre+' '+this.apellido;
    }

}



console.log(persona.nombre); 

console.log(persona.apellido); 

console.log(persona.email); 

console.log(persona.edad); 

console.log(persona); 

console.log(persona.nombreCompleto()); 




console.log('   Ejecucando como un objeto'); 



let persona2 = new Object();            //Debe crear un nuevo objeto en memoria

persona2.nombre = 'Juan';

persona2.direccion = 'Salada 14';

persona2.telefono = '5492618282821' 

console.log(persona2.telefono); 




console.log('     Creamos un nuevo objeto'); 


console.log(persona['apellido']);    //Accedemos como si fuera un arreglo Gil





console.log('     Usamos el ciclo for in'); 
//for in y accedemos al objeto como si fuera un arreglo


for (propiedad in persona){

    console.log(propiedad);

    console.log(persona [propiedad]); 
}





console.log('cambiamos y eliminamos un error') 

persona.apellida = 'Betancud'; //Cambiamos dinamicamente un valor del objeto 

delete persona.apellida; //Eliminamos el error

console.log(persona); 



console.log(' distintas formas de imprimir un objeto');




console.log('nro 1 la mas sencilla concatenar cada valor con cada propiedad');

console.log(persona.nombre+', '+persona.apellido);



console.log('nro 2 a traves del ciclo for in');

for (nombrePropiedad in persona){

    console.log(persona[nombrePropiedad]); 
}


console.log('nro 3 la funcion object.values');

let personaArray = Object.values(persona);

console.log(personaArray);


console.log(' nro 4 utilezamos el metodo JSON.stringify');

let personaString = JSON.stringify(persona);
console.log(personaString);


