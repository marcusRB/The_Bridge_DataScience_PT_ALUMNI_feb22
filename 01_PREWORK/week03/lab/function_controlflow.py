# Convertimos nuestro código en una función python

# Primero definimos una función indicando dos parámetros
# unos es posicional obligatorio y se encuentra a la izquierda
# los nos obligatorios, están a la derecha, y son opcionales o bien
# definidos con valores por defecto, None o cualquier valor

def contar_pasajeros(capacidad, pasajeros_actuales=None):
    """
    Esta función permite contar los pasajeros
    del metro, dada una capacidad y los pasajeros actuales.
    
    Args:
    ----
        capacidad: int, list - posicional
        pasajeros_actuales: default None, opcional - int
    
    Return:
    ------
        números de pasajeros
    """
    if pasajeros_actuales == None:
        pasajeros_actuales = 1
    else:
        if type(capacidad) == list:
            for n in capacidad:
                if type(n) == int and type(pasajeros_actuales) == int:
                    while (pasajeros_actuales < n):
                        pasajeros_actuales += 1
                        print(f"Ha subido un pasajero, el coche tiene {pasajeros_actuales}")
                    print("El metro está lleno")
                else:
                    print("los valores no son numéricos o es otro objeto")


capacidad = [30, 40, 50]
contar_pasajeros(capacidad, pasajeros_actuales=16)

# Devuelve un error de sintaxis al indicar el argumento 
# contar_pasajeros(pasajeros_actuales=10, capacidad)
