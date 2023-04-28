//CREACION ARRAY O ARREGLOS
//Un ARRAY es una colección o agrupación de elementos en una misma variable, 
//cada uno de ellos ubicado por la posición que ocupa en el array. 
//En algunas ocasiones también se les suelen llamar arreglos o vectores

// Sintaxis vieja, ya no se usa y no se recomienda usarla.
//let autos = new Array('Ferrari','Renault','BMW'); 
const autos = ['BMW','Audi','Dodge'];
console.log(autos);

// Recorremos los elementos de un arreglo.
console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++){
    console.log(i + ' : ' + autos[i]);
}

// Modificamos los elementos del arreglo.
autos[2] = 'Mercedes';
console.log(autos[2]);

// Agregar nuevos elementos al arreglo.
// Esto hace que el nuevo elemnto se agregue al final.
autos.push('Ford'); 
console.log(autos);

// Otras formas de agregar elementos al arreglo.
autos[autos.length] = 'Bugatti';
console.log(autos);

// Tercera forma de agregar elementos teniendo CUIDADO.
autos[6] = 'Porsche';
console.log(autos);
 
// Como preguntar si es un Array o Arreglo.
// Devuelve un valor Booleano (True o False)
console.log(Array.isArray(autos));
// Preguntamos si la variable es una instancia de la Clase Array.
console.log(autos instanceof Array);
