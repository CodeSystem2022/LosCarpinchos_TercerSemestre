package mundoPC;

import ar.com.system2023.mundopc.*; // CON * SE IMPORTAN TODAS LAS CLASES

public class mundoPC {
    public static void main(String[] args) {
            Monitor monitorHP = new Monitor("HP", 13); //importar la clase
            Teclado tecladoHP = new Teclado("Bluetooth", "HP");
            Raton ratonHP = new Raton("Bluetooth", "HP");
            Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
            
            //creamos otros objetos de diferente marca
            Monitor monitorGamer = new Monitor("Gamer", 32);
            Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
            Raton ratonGamer = new Raton("Bluetooth", "Gamer");
            Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
            Orden orden1 = new Orden(); //inicializamos el arreglo vacio
            Orden orden2 = new Orden(); //Una nueva lista para el objeto orden2
            orden1.agregarComputadora(computadoraHP); //objetos para lista en orden1, se puede hasta 10 elementos
            orden1.agregarComputadora(computadoraGamer);
            
            Computadora computadorasVarias = new Computadora("Computadoras de diferentes marcas: ", monitorHP, tecladoGamer, ratonHP);
            orden2.agregarComputadora(computadorasVarias);
            
            orden1.mostrarOrden();
            orden2.mostrarOrden();
            
            //agregar mas computadoras de dif marcas //
            //orden 1 lista debe llegar a los 10 elementos
            // probar los metodos al maximo rendimiento
        }
    
}
