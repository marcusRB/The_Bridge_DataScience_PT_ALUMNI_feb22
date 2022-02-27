p_auto_parada=(5,14,8,10)
pasajeros = []
stops = [(2,0), (4,3), (4,2), (2,5)]
n_paradas = len(stops)
p_in=0
p_out=0
maximo=0
for n in range(min(len(stops),len(stops))):
    valor=n
    i=0
    p_in= p_in + stops[n][i]
    p_out= p_out + stops[n][i+1]
    pas= p_in - p_out
    if pas < 0:
        if pas>maximo:
            maximo = pas
            pasajeros.append(pas)
        else:
            pasajeros.append(pas)
    else:
        if pas>maximo:
            maximo = pas
            pasajeros.append(pas)
        else:
            pasajeros.append(pas)
print("El numero de paradas del autobus han sido:",n_paradas)
print("Pasajeros en cada parada",pasajeros)
print("Los pasajeros que han subido a lo largo del trayecto:", p_in)
print("Los pasajeros que han bajado a lo largo del trayecto:", p_out)
print("El maximo de ocupación del autobus durante el trayecto ha sido:",maximo)