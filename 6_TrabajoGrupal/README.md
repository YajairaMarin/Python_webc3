## Modelo de Panel Fotovoltaico (PV)

### Descripción

El archivo PVModel.py contiene el modelo de un panel fotovoltaico (PV) implementado en Python. Este modelo utiliza ecuaciones fotovoltaicas para calcular la corriente, el voltaje y la potencia generados por el panel en función de la irradiancia y la temperatura. Además, se incluye una funcionalidad para almacenar los resultados en una base de datos SQLite3.

## Aplicación Web de Consulta

### Descripción

El archivo main.py implementa una aplicación web utilizando Flask. Esta aplicación permite a los usuarios consultar los resultados almacenados en la base de datos generada por el modelo PV. Los usuarios pueden seleccionar la temperatura e irradiancia deseadas a través de un formulario y obtendrán una tabla con los valores máximos de voltaje, corriente y potencia correspondientes.

### Pasos de ejecución

1. Ejecuta el archivo python PVModel.py, con ello se creará una base de datos llamada data.db. Para saber cuando finaliza la creación del programa se muestra por terminal los valores que estan siendo agregados en la data y esto sólo se realiza en una ocasión.
2. Ejecuta el archivo python main.py y accede a la terminal en tu  navegador por medio del siguiente link:  http://127.0.0.1:5000 
3. Selecciona una temperatura y una irradiancia y luego das clic en el botón buscar.
4. Se mostrará en pantalla los valores de las la temperatura e irradiancia anteriormente seleccionadas junto con el voltaje, corriente y potencia correspondientes.
5. Puedes darle clic al botón volver para realizar una nueva consulta.

## Integrantes de la actividad grupal 

Jenifer Yajaira Marin Olmos 
Rubi Rojas Peralta 
Isidro Mateus Echeverri 