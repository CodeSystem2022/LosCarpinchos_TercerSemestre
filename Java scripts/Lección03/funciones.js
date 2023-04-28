// CLASE 3 - FUNCIONES
// Son códigos reutilizables, se pueden llamar las veces que se requiera.

// Hoisting, llamado de función antes de definirla.
// Mover la declaración de la función al inicio del programa.
miFuncion(8, 2);

// Palabra reservada function.
function miFuncion(a, b){ // Cuerpo de la función.
    // Bloque de la función.
    //console.log("Sumamos: " + (a + b)); 
    return a + b;
}
// Llamado de la función
miFuncion(5, 4); // ingresamos valores a los parámetros.

let resultado = miFuncion(6, 7);
console.log(resultado);

// Declaramos una función de Tipo Expresión o Función Anónima.
let x = function(a , b){return a + b}; // Necesita cierre con punto y coma.
resultado = x(5, 6); // llamada de función, reutilizando la variable resultado.
console.log(resultado);

// Funciones de Tipo Self o Invoking.
(function(a ,b){
    console.log('Ejecutando la funcion: ' + (a + b));
})(9, 4); // No se puede reutulizar, se llama una sola vez.

console.log(typeof miFuncion);

function miFuncionDos(a, b){ 
    console.log(arguments);
    //console.log(arguments.length) // declara cuantos argumentos tiene la función.
}
miFuncionDos(5, 7);// Asignamos valores a la variable.

// toString, convierte la función a Texto.
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto);

// Funciones Flecha (=> operador)
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7); // valor a una variable.
console.log(resultado);

// Diferencia entre Argumentos y Parámetros.
let sumar = function(a = 4, b = 7){
    console.log(arguments[0]); // Muestra el primer parámetro(a) 
    console.log(arguments[1]); // Muestra el segundo parámetro(b)
    //console.log(arguments[2]);
    return a + b + arguments[2];
}
// al pasarle nuevos valores, los valores anteriores se sobreescriben.
resultado = sumar(3, 4, 5); 
console.log(resultado);

// Suma de todos los Argumentos.
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma+= arguments[i]; // arguments es para arreglos.
    }
    return suma;
}

// Paso por Valor, la variable nunca cambia de valor.
// Tipos primitivos.
let k = 10; // variable global.
function cambiarValor(a){ // PASO POR VALOR.
    a = 20; // variable interna de la función.
}
cambiarValor(k);
console.log(k);

// Paso por Referencia.
const persona = { // Definimos un Objeto.
    // Definimos atributos y características.
    nombre: 'Liliana', 
    apellido: 'nievas'    
}
console.log(persona);

function cambiarValorObjeto(p1){
    p1.nombre = 'Lily';
    p1.apellido = 'Jota';
}
cambiarValorObjeto(persona);
console.log(persona);
