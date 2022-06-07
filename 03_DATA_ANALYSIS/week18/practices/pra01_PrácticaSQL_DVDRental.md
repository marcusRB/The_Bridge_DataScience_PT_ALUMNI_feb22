# 02. Práctica SQL - DVD Rental

Practica a realizar en JupyterLab o notebook. Debido a las conexiones concurrente es preferible utilizar vuestra base de datos DVD Rental desde Heroku que tienen creadas. En caso de no tenerla, pueden seguir el tutorial desde material en Classroom.

1. **¿Tenemos actores en la tabla de actores que comparten el nombre completo y, en caso afirmativo, muestran esos nombres compartidos?**

Para responder a esa pregunta, primero necesitamos saber si tenemos actores en la tabla de actores que comparten sus nombres completos. Entonces comenzar contando la cantidad de actores que comparten sus nombres completos.

2. **Muestra los nombres de los clientes que comparten la misma dirección (por ejemplo, esposo y esposa).**

Para responder a esta pregunta, debemos buscar más de un cliente que tenga el mismo address_id pero diferentes customer_ids. Eso significa que haremos JOIN a la tabla de clientes para sí mismo (*autounión*).

3. **Muestra el monto total pagado por todos los clientes en la tabla de pagos.**

Utilizar aquí la función agregada **SUM()** en la columna de monto de la tabla de pagos.

4. **Muestre el monto total pagado por cada cliente en la tabla de pagos.**

5. **¿Cuál es el pago total más alto realizado?**

**6. ¿Cuál es el nombre del cliente que realizó los pagos totales más altos?**

**7. ¿Cuáles son las películas que más se alquilaron?**

**8. Qué películas se han alquilado hasta ahora.**

Debemos entender que no es necesario que ya se hayan alquilado todas las películas de la tabla de películas.

**9. Qué películas no se han alquilado hasta ahora.**

10. **Qué clientes no han alquilado ninguna película hasta ahora.**

Un cliente podría haberse registrado como cliente del lugar de alquiler de DVD, pero aún no ha comenzado a alquilar DVD.

**11. Muestra cada película y la cantidad de veces que se alquila.**

**12. Muestra la cantidad de películas en las que actuó cada actor.**

**13. Muestre los nombres de los actores que actuaron en más de 20 películas.**

**14. ¿Cuántos actores tienen 8 letras solo en sus nombres?**

**15**.**Para todas las películas clasificadas como "PG", muéstrame la película y la cantidad de veces que se alquiló.**

Escribir una subconsulta para seleccionar todos los film_ids que se han alquilado hasta ahora. Para eso, se necesita unir tablas de alquiler e inventario en la columna común Inventory_id.

**16. Muestra las películas que se ofrecen para alquilar en store_id 1 y no se ofrecen en store_id 2. **

**17. Muestre las películas que se ofrecen para alquilar en cualquiera de las dos tiendas 1 y 2.**

**18. Muestra los títulos de las películas que se ofrecen en ambas tiendas al mismo tiempo**

**19. Para cada tienda, muestre el número de clientes que son miembros de esa tienda**

**20. Muestra el título de la película más alquilada en la tienda con store_id 1**

**21. Cuántas películas aún no se ofrecen para alquilar en las tiendas. Hay dos tiendas solo 1 y 2**

**22. Muestre los customer_id para aquellos clientes que alquilaron un DVD de películas más de una vez.**

Para responder a esta pregunta, primero debemos conocer los film_ids que alquiló cada cliente.

**23. Muestra la cantidad de películas alquiladas en cada clasificación.**

Para responder a esta pregunta, primero debemos conocer los ID de película que se alquilaron (unir tablas de alquiler e inventario) y las calificaciones de cada película (unir tabla de películas).

**24. Muestre el beneficio de cada una de las tiendas 1 y 2.**

Para responder a esta pregunta, necesitamos saber la cantidad pagada y el Inventory_id para cada película alquilada al unirse (tablas de alquiler y pago) y el store_id para esa transacción de alquiler (unirse a la tabla de inventario).

**25.  Muestra el beneficio de cada una de las tiendas 1 y 2 seguido del beneficio total de ambas tiendas**

**26. Cuente la cantidad de actores cuyos nombres no comienzan con una "A"**

**27. Busque el nombre del actor que comience con "P" seguido de (una *e* o una *a*) y luego cualquier otra letra**

**28. Busque nombres de clientes que comiencen con "P" seguido de 5 letras**

**29. Busque actores con PaRkEr como su nombre e ignore las letras mayúsculas y minúsculas. Luego seleccione actores llamados PaRkEr y haga coincidir el caso de la letra**

**30. Busque nombres de actores que comiencen con "P" seguidos de cualquier letra de la a a la e y luego de cualquier otra letra**

