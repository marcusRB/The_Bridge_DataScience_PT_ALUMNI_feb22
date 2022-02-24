# durante la fase de programación y testing o debugging, pausamos la evaluación
capacidad_metro = 100000000
pasajeros_actuales = 15

while True:
    if (pasajeros_actuales < capacidad_metro):
        pasajeros_actuales += 1
        print(f"Ha subido un pasajero, el coche tiene {pasajeros_actuales}")
        if pasajeros_actuales == 20:
            break;
print("El metro está lleno")