# Temperatura del procesador

Tenemos un sensor de temperatura en el procesador el servidor de nuestra empresa. Queremos analizar los datos proporcionados para analizar si debemos cambiar de sistema de refrigeración por uno mejor. Es caro y como analista de datos no podemos tomar decisiones sin base. 

Proporcionamos las temperaturas medidas a lo largo de las 24 horas de un día en una estructura de datos tipo lista compuesta de 24 números enteros: 
```
temperaturas_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
```

## Problema

Si el sensor detecta más de 4 horas con temperaturas mayores o igual que 70ºC o alguna temperatura superior a 80ºC o la media fuera superior a 65ºC a lo largo de todo el día, deberemos dar la orden de cambiar el sistema de refrigeración para evitar dañar el procesador. 

Te vamos a guiar paso a paso para que puedas tomar la decisión calculando algunos pasos intermedios: 

1. Temperatura mínima
2. Temperatura máxima
3. Temperaturas igual o superior a 70ºC
4. Media de temperaturas a lo largo del día. 
5. Si hubiera un fallo en el sensor a las 03:00 y no capturáramos el dato, ¿Cómo estímarias el valor que nos falta? Corrige ese valor en la lista de temperaturas. 
6. Bonus: Nuestro personal de mantenimiento es de Estados Unidos y no entiende el sistema métrico internacional. Pása las temperaturas a Grados Fahrenheit.

Fórmula: F = 1.8 * C + 32

web: https://es.wikipedia.org/wiki/Grado_Fahrenheit

## Toma la decisión
Recuerda que si el sensor detecta más de 4 horas con temperaturas mayores o igual que 70ºC o alguna temperatura superior a 80ºC o la media fuera superior a 65ºC a lo largo de todo el día, deberemos dar la orden de cambiar el sistema de refrigeración para evitar el peligro de dañar el equipamiento: 
* más de 4 horas con temperaturas mayores o igual que 70ºC
* alguna temperatura superior a 80ºC
* media fuera superior a 65ºC a lo largo de todo el día
Si se cumple alguna de estas tres habrá que cambiar el sistema de refrigeración. 

## Objetivos
1. Tratamiento de listas
2. Uso de bucle o list comprenhention
3. Cálculo de la media, minimo y máximo. 
4. Filtrado de listas. 
5. Interpolar un valor atípico. 
6. Operadores lógicos. 
7. Imprimir por consola