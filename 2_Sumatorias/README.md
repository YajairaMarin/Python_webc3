# Tiempo de ejecución y rendimiento: Suma Constante vs Suma Lineal

Este script de Python compara el tiempo de ejecución de dos funciones diferentes que permiten calcular la suma de los primeros n números naturales. La primera función utiliza la fórmula de la suma constante, mientras que la segunda utiliza un bucle para sumar los números.

## Funciones

### funcion1(n)
Calcula la suma de los primeros n números naturales utilizando la fórmula de la suma constante: (n * (n + 1)) // 2.

### funcion2(n)
Calcula la suma de los primeros n números naturales utilizando un bucle for y acumulando la suma linealmente.

## Números de Prueba

El script realiza mediciones de tiempo para las funciones utilizando una lista de números de prueba: [100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000].

## Medición de Tiempos

El script mide los tiempos de ejecución de ambas funciones para cada número de prueba y presenta los resultados en segundos.

## Resultados

Los resultados se imprimen en la consola y se almacenan en un DataFrame de Pandas. Además, se genera un gráfico en formato png que compara los tiempos de ejecución de ambas funciones en función del número de elementos.

## Captura de imagen

la imagen se guarda en la carpeta donde se ejecuta el  script, con nombre "sumatorias.png".